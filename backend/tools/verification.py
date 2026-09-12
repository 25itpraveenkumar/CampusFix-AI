"""
Verification tool for CampusFix AI.

Checks whether a simulated issue has been resolved.
"""

from typing import Any


def verify_issue(
    issue: str,
    location: str,
    action_completed: bool,
) -> dict[str, Any]:
    """Verify whether the simulated issue was resolved."""

    if not isinstance(issue, str) or not issue.strip():
        return {
            "success": False,
            "tool": "verification",
            "status": "invalid_input",
            "message": "Issue must be a non-empty string.",
            "data": {},
        }

    if not isinstance(location, str) or not location.strip():
        return {
            "success": False,
            "tool": "verification",
            "status": "invalid_input",
            "message": "Location must be a non-empty string.",
            "data": {},
        }

    if not isinstance(action_completed, bool):
        return {
            "success": False,
            "tool": "verification",
            "status": "invalid_input",
            "message": "action_completed must be a boolean.",
            "data": {},
        }

    if action_completed:
        return {
            "success": True,
            "tool": "verification",
            "status": "verified",
            "message": "Simulated verification confirms that the issue is resolved.",
            "data": {
                "issue": issue.strip(),
                "location": location.strip(),
                "resolved": True,
            },
        }

    return {
        "success": True,
        "tool": "verification",
        "status": "not_resolved",
        "message": "Simulated verification indicates that the issue is not resolved.",
        "data": {
            "issue": issue.strip(),
            "location": location.strip(),
            "resolved": False,
        },
    }