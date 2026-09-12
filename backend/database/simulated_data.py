"""
Deterministic simulated campus data for CampusFix AI.

This module contains mock data only.
It does not connect to real campus infrastructure.
"""

CAMPUS_KNOWLEDGE = {
    "wifi": {
        "known_issue": "Wi-Fi connectivity problem",
        "troubleshooting_steps": [
            "Check whether the affected access point is available.",
            "Check network connectivity.",
            "Check DNS resolution.",
            "Verify connectivity again after troubleshooting.",
        ],
        "relevant_equipment": [
            "Wireless Access Point",
            "Network Gateway",
            "DNS Service",
        ],
    },
    "printer": {
        "known_issue": "Printer service problem",
        "troubleshooting_steps": [
            "Check printer service status.",
            "Check printer connectivity.",
            "Verify printer availability.",
        ],
        "relevant_equipment": [
            "Network Printer",
            "Print Server",
        ],
    },
    "projector": {
        "known_issue": "Projector service problem",
        "troubleshooting_steps": [
            "Check projector power status.",
            "Check display connection.",
            "Verify projector availability.",
        ],
        "relevant_equipment": [
            "Projector",
            "Display Cable",
        ],
    },
}


SERVICE_STATUS = {
    "wifi": {
        "status": "degraded",
        "message": "Simulated Wi-Fi service is degraded in Lab 3.",
        "affected_locations": ["Lab 3"],
    },
    "dns": {
        "status": "operational",
        "message": "Simulated DNS service is operational.",
        "affected_locations": [],
    },
    "dhcp": {
        "status": "operational",
        "message": "Simulated DHCP service is operational.",
        "affected_locations": [],
    },
    "network_gateway": {
        "status": "operational",
        "message": "Simulated network gateway is operational.",
        "affected_locations": [],
    },
    "printer": {
        "status": "operational",
        "message": "Simulated printer service is operational.",
        "affected_locations": [],
    },
    "projector": {
        "status": "operational",
        "message": "Simulated projector service is operational.",
        "affected_locations": [],
    },
}


SIMULATED_LOCATIONS = [
    "Lab 1",
    "Lab 2",
    "Lab 3",
    "Library",
    "Admin Block",
    "Seminar Hall",
]