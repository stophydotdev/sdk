from __future__ import annotations

from typing import Any, Optional


class StophyError(Exception):
    """Raised when the Stophy API responds with a non-2xx status."""

    def __init__(
        self,
        message: str,
        *,
        status: int,
        code: Optional[str] = None,
        request_id: Optional[str] = None,
        details: Any = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.request_id = request_id
        self.details = details
