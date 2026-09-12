"""
Knowledge tool for CampusFix AI.

Provides simulated troubleshooting information for campus issues.
This tool does not make decisions or perform agent reasoning.
"""

from typing import Any

from backend.database.simulated_data import CAMPUS_KNOWLEDGE


def get_knowledge(issue: str, location: str) -> dict[str, Any]:
    """
    Return troubleshooting knowledge for a campus issue.

    Args:
        issue: The reported issue, such as "wifi", "printer", or "projector".
        location: The campus location where the issue was reported.

    Returns:
        A structured, JSON-compatible result.
    """

    if not isinstance(issue, str) or not issue.strip():
        return {
            "success": False,
            "tool": "knowledge",
            "status": "invalid_input",
            "message": "Issue must be a non-empty string.",
            "data": {},
        }

    if not isinstance(location, str) or not location.strip():
        return {
            "success": False,
            "tool": "knowledge",
            "status": "invalid_input",
            "message": "Location must be a non-empty string.",
            "data": {},
        }

    issue_key = issue.strip().lower()

    knowledge = CAMPUS_KNOWLEDGE.get(issue_key)

    if knowledge is None:
        return {
            "success": False,
            "tool": "knowledge",
            "status": "not_found",
            "message": f"No simulated knowledge found for issue '{issue.strip()}'.",
            "data": {
                "location": location.strip(),
            },
        }

    return {
        "success": True,
        "tool": "knowledge",
        "status": "success",
        "message": "Simulated troubleshooting knowledge retrieved.",
        "data": {
            "location": location.strip(),
            "known_issue": knowledge["known_issue"],
            "troubleshooting_steps": knowledge["troubleshooting_steps"],
            "relevant_equipment": knowledge["relevant_equipment"],
        },
    }