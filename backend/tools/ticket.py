"""
Ticket and escalation tool for CampusFix AI.

Creates simulated support tickets.
"""

from typing import Any
import uuid


def create_ticket(
    location: str,
    issue: str,
    priority: str,
    description: str,
) -> dict[str, Any]:
    """Create a simulated support ticket."""

    if not isinstance(location, str) or not location.strip():
        return {
            "success": False,
            "tool": "ticket",
            "status": "invalid_input",
            "message": "Location must be a non-empty string.",
            "data": {},
        }

    if not isinstance(issue, str) or not issue.strip():
        return {
            "success": False,
            "tool": "ticket",
            "status": "invalid_input",
            "message": "Issue must be a non-empty string.",
            "data": {},
        }

    if priority not in {"low", "medium", "high", "critical"}:
        return {
            "success": False,
            "tool": "ticket",
            "status": "invalid_input",
            "message": "Priority must be low, medium, high, or critical.",
            "data": {},
        }

    if not isinstance(description, str) or not description.strip():
        return {
            "success": False,
            "tool": "ticket",
            "status": "invalid_input",
            "message": "Description must be a non-empty string.",
            "data": {},
        }

    ticket_id = f"TKT-{uuid.uuid4().hex[:8].upper()}"

    return {
        "success": True,
        "tool": "ticket",
        "status": "created",
        "message": "Simulated support ticket created successfully.",
        "data": {
            "ticket_id": ticket_id,
            "location": location.strip(),
            "issue": issue.strip(),
            "priority": priority,
            "description": description.strip(),
            "status": "open",
        },
    }