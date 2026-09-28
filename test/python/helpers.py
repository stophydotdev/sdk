from __future__ import annotations

import json
from typing import Any, Dict, List, Tuple, Union

import httpx

from stophy import Stophy


def make_client(
    responses: Union[Dict[str, Any], List[Dict[str, Any]]],
    **opts: Any,
) -> Tuple[Stophy, List[httpx.Request]]:
    """A Stophy client backed by a mock transport, plus the requests it records.

    Each response spec is ``{"status": int, "json": ..., "raw": str, "headers": {}}``.
    Pass a list to vary the reply per call; the last entry repeats.
    """
    queue = list(responses) if isinstance(responses, list) else [responses]
    calls: List[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        spec = queue.pop(0) if len(queue) > 1 else queue[0]
        headers = spec.get("headers", {})
        status = spec.get("status", 200)
        if "raw" in spec:
            return httpx.Response(status, headers=headers, text=spec["raw"])
        return httpx.Response(status, headers=headers, json=spec.get("json"))

    kwargs = {"api_key": "sk_test", "max_retries": 0, **opts}
    client = Stophy(transport=httpx.MockTransport(handler), **kwargs)
    return client, calls


def body_of(request: httpx.Request) -> Any:
    return json.loads(request.content) if request.content else None


def query_of(request: httpx.Request) -> Dict[str, str]:
    return dict(request.url.params)


def ok(data: Any) -> Dict[str, Any]:
    return {"json": {"success": True, "requestId": "req_1", "data": data}}
