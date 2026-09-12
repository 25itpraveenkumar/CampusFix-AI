"""
Service status tool for CampusFix AI.

Returns simulated status information for campus services.
"""

from typing import Any

from backend.database.simulated_data import SERVICE_STATUS


def get_service_status(service: str) -> dict[str, Any]:
    """
    Return the simulated status of a campus service.
    """

    if not isinstance(service, str) or not service.strip():
        return {
            "success": False,
            "tool": "service_status",
            "status": "invalid_input",
            "message": "Service must be a non-empty string.",
            "data": {},
        }

    service_key = service.strip().lower()

    service_data = SERVICE_STATUS.get(service_key)

    if service_data is None:
        return {
            "success": False,
            "tool": "service_status",
            "status": "not_found",
            "message": f"No simulated service found for '{service.strip()}'.",
            "data": {},
        }

    return {
        "success": True,
        "tool": "service_status",
        "status": "success",
        "message": "Simulated service status retrieved.",
        "data": {
            "service": service_key,
            "service_status": service_data["status"],
            "details": service_data["message"],
            "affected_locations": service_data["affected_locations"],
        },
    }