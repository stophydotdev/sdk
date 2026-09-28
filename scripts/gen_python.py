#!/usr/bin/env python3
"""Generate the Python client surface and models from openapi.json.

Run from the repo root:

    uv run --project packages/python python scripts/gen_python.py
"""

from __future__ import annotations

import json
import keyword
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "openapi.json"
OUT_DIR = ROOT / "packages" / "python" / "src" / "stophy" / "generated"

IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def pascal(value: str) -> str:
    parts = re.split(r"[^A-Za-z0-9]+", value)
    return "".join(part[:1].upper() + part[1:] for part in parts if part) or "Model"


def snake(value: str) -> str:
    value = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    return value.lower()


def param_name(key: str) -> str:
    name = snake(key)
    if keyword.iskeyword(name):
        name += "_"
    if not IDENT.match(name):
        raise SystemExit(f"Cannot use {key!r} as a Python parameter.")
    return name


def literal(value: Any) -> str:
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=True)
    if isinstance(value, bool):
        return "True" if value else "False"
    if value is None:
        return "None"
    if isinstance(value, (int, float)):
        return repr(value)
    raise SystemExit(f"Unsupported literal {value!r}.")


class Emitter:
    def __init__(self, components: dict[str, Any]) -> None:
        self.components = components
        self.cache: dict[str, str] = {}
        self.used: set[str] = set()
        self.aliases: list[tuple[str, list[Any]]] = []
        self.models: list[tuple[str, list[tuple[str, str, bool]]]] = []

    def fresh(self, hint: str) -> str:
        name = hint
        number = 2
        while name in self.used:
            name = f"{hint}{number}"
            number += 1
        self.used.add(name)
        return name

    def py_type(self, schema: Any, hint: str) -> str:
        if not isinstance(schema, dict):
            return "Any"
        if "$ref" in schema:
            return self.ref_type(schema["$ref"], hint)
        options = schema.get("oneOf", schema.get("anyOf"))
        if isinstance(options, list) and options:
            consts: list[Any] = []
            for option in options:
                if isinstance(option, dict) and "const" in option and "enum" not in option:
                    consts.append(option["const"])
                else:
                    consts = []
                    break
            if consts:
                return self.literal_alias(hint, consts)
            parts: list[str] = []
            for index, option in enumerate(options):
                part = self.py_type(option, f"{hint}Option{index}")
                if part not in parts:
                    parts.append(part)
            return parts[0] if len(parts) == 1 else " | ".join(parts)
        if isinstance(schema.get("enum"), list):
            return self.literal_alias(hint, schema["enum"])
        if "const" in schema:
            return f"Literal[{literal(schema['const'])}]"
        kind = schema.get("type")
        if isinstance(kind, list):
            rest = [item for item in kind if item != "null"]
            if len(rest) != 1 or not isinstance(rest[0], str):
                return "Any"
            inner = self.py_type({**schema, "type": rest[0]}, hint)
            return f"{inner} | None" if "null" in kind else inner
        if kind == "string":
            return "str"
        if kind == "integer":
            return "int"
        if kind == "number":
            return "float"
        if kind == "boolean":
            return "bool"
        if kind == "null":
            return "None"
        if kind == "array":
            return f"list[{self.py_type(schema.get('items', {}), hint + 'Item')}]"
        if kind == "object" or "properties" in schema:
            return self.object_type(schema, hint)
        return "Any"

    def ref_type(self, ref: Any, hint: str) -> str:
        if not isinstance(ref, str) or not ref.startswith("#/components/schemas/"):
            return "Any"
        name = ref.rsplit("/", 1)[-1]
        schema = self.components.get(name)
        if schema is None:
            return "Any"
        return self.object_type(schema, pascal(name) or hint)

    def object_type(self, schema: dict[str, Any], hint: str) -> str:
        properties = schema.get("properties")
        if not isinstance(properties, dict) or not properties:
            extra = schema.get("additionalProperties", True)
            if extra is True or extra is False or extra is None:
                return "dict[str, Any]"
            return f"dict[str, {self.py_type(extra, hint + 'Value')}]"
        canonical = json.dumps(schema, sort_keys=True, separators=(",", ":"))
        cached = self.cache.get(canonical)
        if cached is not None:
            return cached
        name = self.fresh(hint)
        self.cache[canonical] = name
        required = set(schema.get("required") or [])
        fields: list[tuple[str, str, bool]] = []
        for key, prop in properties.items():
            if not isinstance(key, str):
                raise SystemExit(f"{name} has a non-string field.")
            fields.append((key, self.py_type(prop, name + pascal(key)), key in required))
        self.models.append((name, fields))
        return name

    def literal_alias(self, hint: str, values: list[Any]) -> str:
        canonical = json.dumps(values, separators=(",", ":"))
        cached = self.cache.get("literal:" + canonical)
        if cached is not None:
            return cached
        name = self.fresh(hint)
        self.cache["literal:" + canonical] = name
        self.aliases.append((name, values))
        return name


def response_schema(operation: dict[str, Any]) -> Any:
    responses = operation.get("responses")
    if not isinstance(responses, dict):
        raise SystemExit(f"{operation.get('operationId')} has no responses.")
    ok = responses.get("200")
    if not isinstance(ok, dict):
        raise SystemExit(f"{operation.get('operationId')} has no 200 response.")
    content = ok.get("content")
    if not isinstance(content, dict):
        raise SystemExit(f"{operation.get('operationId')} has no 200 content.")
    json_content = content.get("application/json")
    if not isinstance(json_content, dict) or "schema" not in json_content:
        raise SystemExit(f"{operation.get('operationId')} has no JSON schema.")
    return json_content["schema"]


def body_schema(operation: dict[str, Any]) -> dict[str, Any] | None:
    body = operation.get("requestBody")
    if not isinstance(body, dict):
        return None
    content = body.get("content")
    if not isinstance(content, dict):
        return None
    json_content = content.get("application/json")
    if not isinstance(json_content, dict):
        return None
    schema = json_content.get("schema")
    return schema if isinstance(schema, dict) else None


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.operation: dict[str, Any] | None = None
        self.children: dict[str, Node] = {}


def build_tree(operations: list[dict[str, Any]]) -> Node:
    root = Node("")
    for operation in operations:
        node = root
        for segment in operation["segments"]:
            node = node.children.setdefault(segment, Node(segment))
        node.operation = operation
    return root


def render_models(emitter: Emitter) -> str:
    used_literal = bool(emitter.aliases)
    used_not_required = any(
        not required for _, fields in emitter.models for _, _, required in fields
    )
    typing_names = ["Any", "Literal"] if used_literal else ["Any"]
    extensions = ["NotRequired", "TypedDict"] if used_not_required else ["TypedDict"]
    body = [
        '"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""',
        "",
        "from __future__ import annotations",
        "",
        f"from typing import {', '.join(typing_names)}",
        "",
        f"from typing_extensions import {', '.join(extensions)}",
        "",
    ]
    for name, values in emitter.aliases:
        body.append(f"{name} = Literal[")
        for value in values:
            body.append(f"    {literal(value)},")
        body.append("]")
        body.append("")
    functional = [
        (name, fields)
        for name, fields in emitter.models
        if any(keyword.iskeyword(key) for key, _, _ in fields)
    ]
    classes = [
        (name, fields)
        for name, fields in emitter.models
        if not any(keyword.iskeyword(key) for key, _, _ in fields)
    ]
    for name, fields in functional:
        body.append(f"{name} = TypedDict(")
        body.append(f'    "{name}",')
        body.append("    {")
        for key, typ, required in fields:
            annotation = typ if required else f"NotRequired[{typ}]"
            body.append(f'        "{key}": {annotation},')
        body.append("    },")
        body.append(")")
        body.append("")
    for name, fields in classes:
        body.append(f"class {name}(TypedDict):")
        if not fields:
            body.append("    pass")
        for key, typ, required in fields:
            if not IDENT.match(key):
                raise SystemExit(f"{name}.{key} is not a Python identifier.")
            annotation = typ if required else f"NotRequired[{typ}]"
            body.append(f"    {key}: {annotation}")
        body.append("")
        body.append("")
    return "\n".join(body).rstrip() + "\n"


def render_signature(
    params: list[dict[str, Any]],
    response: str,
    *,
    overload: str | None,
    async_mode: bool,
) -> list[str]:
    prefix = "async def" if async_mode else "def"
    lines = [f"    {prefix} __call__("]
    lines.append("        self,")
    lines.append("        *,")
    for param in params:
        if param["required"]:
            lines.append(f"        {param['name']}: {param['type']},")
        else:
            lines.append(f"        {param['name']}: {param['type']} | None = None,")
    if overload == "markdown":
        lines.append('        format: Literal["markdown"],')
        lines.append("    ) -> str: ...")
        return lines
    if overload == "json":
        lines.append("        format: None = None,")
        lines.append(f"    ) -> {response}: ...")
        return lines
    lines.append('        format: Literal["markdown"] | None = None,')
    lines.append(f"    ) -> {response} | str:")
    return lines


def render_method(operation: dict[str, Any], *, async_mode: bool) -> list[str]:
    lines: list[str] = []
    for kind in ("markdown", "json"):
        lines.append("    @overload")
        lines.extend(
            render_signature(
                operation["params"],
                operation["response"],
                overload=kind,
                async_mode=async_mode,
            )
        )
    lines.extend(
        render_signature(
            operation["params"],
            operation["response"],
            overload=None,
            async_mode=async_mode,
        )
    )
    if operation["method"] == "GET":
        lines.append("        body = None")
    elif operation["params"]:
        lines.append("        body = _omit_none({")
        for param in operation["params"]:
            lines.append(f'            "{param["json"]}": {param["name"]},')
        lines.append("        })")
    else:
        lines.append("        body = {}")
    call = "await self._call" if async_mode else "self._call"
    lines.append(
        f'        return {call}("{operation["method"]}", "{operation["path"]}", body, format)'
    )
    return lines


def class_name(prefix: str, parts: list[str]) -> str:
    return prefix + "".join(pascal(part) for part in parts)


def render_class(node: Node, parts: list[str], prefix: str, async_mode: bool) -> list[str]:
    lines: list[str] = []
    for child in node.children.values():
        lines.extend(render_class(child, [*parts, child.name], prefix, async_mode))
    name = class_name(prefix, parts)
    call_name = "AsyncCall" if async_mode else "SyncCall"
    lines.append(f"class {name}:")
    for child_name, _child in node.children.items():
        lines.append(f"    {child_name}: {class_name(prefix, [*parts, child_name])}")
    lines.append(f"    def __init__(self, call: {call_name}) -> None:")
    lines.append("        self._call = call")
    for child_name in node.children:
        lines.append(
            f"        self.{child_name} = {class_name(prefix, [*parts, child_name])}(call)"
        )
    if node.operation is not None:
        lines.extend(render_method(node.operation, async_mode=async_mode))
    lines.append("")
    lines.append("")
    return lines


def render_root(root: Node, prefix: str, async_mode: bool) -> list[str]:
    lines: list[str] = []
    for child in root.children.values():
        lines.extend(render_class(child, [child.name], prefix, async_mode))
    call_name = "AsyncCall" if async_mode else "SyncCall"
    class_name_root = "AsyncSurface" if async_mode else "SyncSurface"
    lines.append(f"class {class_name_root}:")
    for child_name in root.children:
        lines.append(f"    {child_name}: {class_name(prefix, [child_name])}")
    lines.append(f"    def __init__(self, call: {call_name}) -> None:")
    for child_name in root.children:
        lines.append(f"        self.{child_name} = {class_name(prefix, [child_name])}(call)")
    lines.append("")
    return lines


def render_namespaces(source: str) -> str:
    header = [
        '"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, Literal, Mapping, Protocol, overload",
        "",
        "",
    ]
    return "\n".join(header) + source


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text())
    components = spec.get("components", {}).get("schemas", {})
    if not isinstance(components, dict):
        raise SystemExit("OpenAPI components.schemas is missing.")
    emitter = Emitter(components)
    prepared: list[dict[str, Any]] = []
    for path, item in spec["paths"].items():
        if not isinstance(item, dict):
            continue
        for method in ("get", "post"):
            operation = item.get(method)
            if not isinstance(operation, dict):
                continue
            operation_id = operation.get("operationId")
            if not isinstance(operation_id, str):
                raise SystemExit(f"{method.upper()} {path} is missing operationId.")
            segments = [part for part in path.split("/") if part and part != "v1"]
            schema = body_schema(operation)
            properties = schema.get("properties", {}) if schema else {}
            required = set(schema.get("required", []) if schema else [])
            if not isinstance(properties, dict):
                properties = {}
            params = []
            for key, prop in properties.items():
                params.append(
                    {
                        "json": key,
                        "name": param_name(key),
                        "required": key in required,
                        "type": emitter.py_type(prop, pascal(operation_id) + pascal(key)),
                    }
                )
            prepared.append(
                {
                    "id": operation_id,
                    "method": method.upper(),
                    "path": path,
                    "segments": segments,
                    "params": params,
                    "response": emitter.py_type(
                        response_schema(operation),
                        pascal(operation_id) + "Response",
                    ),
                }
            )

    models = render_models(emitter)
    tree = build_tree(prepared)
    body = [
        "",
        "class SyncCall(Protocol):",
        "    def __call__(",
        "        self,",
        "        method: str,",
        "        path: str,",
        "        body: Mapping[str, Any] | None,",
        "        format: str | None,",
        "    ) -> Any: ...",
        "",
        "",
        "class AsyncCall(Protocol):",
        "    async def __call__(",
        "        self,",
        "        method: str,",
        "        path: str,",
        "        body: Mapping[str, Any] | None,",
        "        format: str | None,",
        "    ) -> Any: ...",
        "",
        "",
        "def _omit_none(values: Mapping[str, Any]) -> dict[str, Any]:",
        "    return {key: value for key, value in values.items() if value is not None}",
        "",
        "",
    ]
    body.extend(render_root(tree, "Sync", False))
    body.extend(render_root(tree, "Async", True))
    namespaces = "\n".join(body)
    model_names = {name for name, _ in emitter.models} | {name for name, _ in emitter.aliases}
    used = set(re.findall(r"\b[A-Z][A-Za-z0-9_]*\b", namespaces)) & model_names
    import_block = ""
    if used:
        joined = ",\n    ".join(sorted(used, key=str.casefold))
        import_block = f"from .models import (\n    {joined},\n)\n\n"
    text = render_namespaces(import_block + namespaces)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "__init__.py").write_text(
        '"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""\n'
    )
    (OUT_DIR / "models.py").write_text(models)
    (OUT_DIR / "namespaces.py").write_text(text)
    print(f"Wrote {len(prepared)} operations and {len(emitter.models)} models.")


if __name__ == "__main__":
    main()
