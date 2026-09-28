from __future__ import annotations

from typing import Any, NoReturn, TypedDict

from .errors import StophyError


class Usage(TypedDict):
    balanceMicros: int
    creditsUsed: int
    requestCount: int


class LogEntry(TypedDict):
    apiKeyId: str | None
    apiKeyName: str | None
    createdAt: str
    credits: int
    durationMs: int | None
    endpoint: str
    id: str
    method: str
    response: str
    status: int


class Logs(TypedDict):
    endpoints: list[str]
    logs: list[LogEntry]
    page: int
    pageSize: int
    total: int
    totalPages: int


def parse_usage(value: Any) -> Usage:
    if not isinstance(value, dict):
        _unexpected("usage")
    return {
        "balanceMicros": _int(value, "balanceMicros"),
        "creditsUsed": _int(value, "creditsUsed"),
        "requestCount": _int(value, "requestCount"),
    }


def parse_logs(value: Any) -> Logs:
    if not isinstance(value, dict) or not isinstance(value.get("logs"), list):
        _unexpected("logs")
    endpoints = value.get("endpoints")
    if not isinstance(endpoints, list) or not all(isinstance(item, str) for item in endpoints):
        _unexpected("logs.endpoints")
    return {
        "endpoints": endpoints,
        "logs": [_log(item) for item in value["logs"]],
        "page": _int(value, "page"),
        "pageSize": _int(value, "pageSize"),
        "total": _int(value, "total"),
        "totalPages": _int(value, "totalPages"),
    }


def _log(value: Any) -> LogEntry:
    if not isinstance(value, dict):
        _unexpected("logs.logs")
    return {
        "apiKeyId": _str_or_none(value, "apiKeyId"),
        "apiKeyName": _str_or_none(value, "apiKeyName"),
        "createdAt": _str(value, "createdAt"),
        "credits": _int(value, "credits"),
        "durationMs": _int_or_none(value, "durationMs"),
        "endpoint": _str(value, "endpoint"),
        "id": _str(value, "id"),
        "method": _str(value, "method"),
        "response": _str(value, "response"),
        "status": _int(value, "status"),
    }


def _int(record: dict[str, Any], field: str) -> int:
    value = record.get(field)
    if isinstance(value, bool) or not isinstance(value, int):
        _unexpected(field)
    return value


def _int_or_none(record: dict[str, Any], field: str) -> int | None:
    value = record.get(field)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        _unexpected(field)
    return value


def _str(record: dict[str, Any], field: str) -> str:
    value = record.get(field)
    if not isinstance(value, str):
        _unexpected(field)
    return value


def _str_or_none(record: dict[str, Any], field: str) -> str | None:
    value = record.get(field)
    if value is None:
        return None
    if not isinstance(value, str):
        _unexpected(field)
    return value


def _unexpected(field: str) -> NoReturn:
    raise StophyError(
        f"Stophy returned an unexpected {field}",
        status=200,
        retryable=False,
    )
