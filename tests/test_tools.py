from backend.tools.knowledge import get_knowledge
from backend.tools.service_status import get_service_status
from backend.tools.diagnostic import run_diagnostic
from backend.tools.verification import verify_issue
from backend.tools.ticket import create_ticket


def test_knowledge_lookup():
    result = get_knowledge("wifi", "Lab 3")

    assert result["success"] is True
    assert result["tool"] == "knowledge"
    assert result["status"] == "success"
    assert result["data"]["location"] == "Lab 3"


def test_service_status():
    result = get_service_status("wifi")

    assert result["success"] is True
    assert result["tool"] == "service_status"
    assert result["status"] == "success"


def test_diagnostic_insufficient():
    result = run_diagnostic(
        "connectivity_check",
        "Lab 3",
        1,
    )

    assert result["success"] is True
    assert result["status"] == "insufficient"


def test_diagnostic_success():
    result = run_diagnostic(
        "connectivity_check",
        "Lab 3",
        2,
    )

    assert result["success"] is True
    assert result["status"] == "success"


def test_verification():
    result = verify_issue(
        "wifi",
        "Lab 3",
        True,
    )

    assert result["success"] is True
    assert result["status"] == "verified"
    assert result["data"]["resolved"] is True


def test_ticket_creation():
    result = create_ticket(
        "Lab 3",
        "wifi",
        "high",
        "Wi-Fi issue remains unresolved.",
    )

    assert result["success"] is True
    assert result["status"] == "created"
    assert result["data"]["priority"] == "high"
    assert result["data"]["status"] == "open"


def test_invalid_knowledge_input():
    result = get_knowledge("", "Lab 3")

    assert result["success"] is False
    assert result["status"] == "invalid_input"


def test_invalid_service_input():
    result = get_service_status("unknown_service")

    assert result["success"] is False
    assert result["status"] == "not_found"


def test_invalid_ticket_priority():
    result = create_ticket(
        "Lab 3",
        "wifi",
        "urgent",
        "Test ticket",
    )

    assert result["success"] is False
    assert result["status"] == "invalid_input"