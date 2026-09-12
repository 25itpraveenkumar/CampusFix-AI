"""
Diagnostic tool for CampusFix AI.

Provides deterministic simulated diagnostic results.
"""

from typing import Any


def run_diagnostic(
    check: str,
    location: str,
    attempt: int = 1,
) -> dict[str, Any]:
    """Run a simulated diagnostic check."""

    if not isinstance(check, str) or not check.strip():
        return {
            "success": False,
            "tool": "diagnostic",
            "status": "invalid_input",
            "message": "Diagnostic check must be a non-empty string.",
            "data": {},
        }

    if not isinstance(location, str) or not location.strip():
        return {
            "success": False,
            "tool": "diagnostic",
            "status": "invalid_input",
            "message": "Location must be a non-empty string.",
            "data": {},
        }

    if check.strip().lower() not in {
        "connectivity_check",
        "ping_check",
        "dns_check",
        "access_point_check",
    }:
        return {
            "success": False,
            "tool": "diagnostic",
            "status": "not_found",
            "message": f"Unknown diagnostic check '{check.strip()}'.",
            "data": {},
        }

    # Intentional simulated failure on the first attempt.
    if attempt == 1:
        return {
            "success": True,
            "tool": "diagnostic",
            "status": "insufficient",
            "message": "Initial diagnostic result is insufficient. A further check is required.",
            "data": {
                "check": check.strip().lower(),
                "location": location.strip(),
                "attempt": attempt,
            },
        }

    return {
        "success": True,
        "tool": "diagnostic",
        "status": "success",
        "message": "Simulated diagnostic check completed successfully.",
        "data": {
            "check": check.strip().lower(),
            "location": location.strip(),
            "attempt": attempt,
            "result": "Diagnostic check passed.",
        },
    }