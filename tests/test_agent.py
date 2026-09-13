from backend.agents.agent import Agent
from backend.agents.state import AgentState


class FakeTool:
    def __init__(self, result):
        self.result = result

    def execute(self, state):
        return self.result


def test_agent_resolves_successfully():

    tools = {
        "check_service_status": FakeTool({
            "success": True,
            "message": "Wi-Fi service is available."
        }),
        "verification": FakeTool({
            "success": True,
            "message": "Wi-Fi is working now."
        })
    }

    state = AgentState(
        original_goal="The Wi-Fi in Lab 3 isn't working.",
        location="Lab 3",
        issue_type="wifi"
    )

    agent = Agent(tools)

    result = agent.run(state)

    assert result.status == "RESOLVED"
    assert result.final_result == "Wi-Fi is working now."


def test_agent_replans_after_failure():

    tools = {
        "check_service_status": FakeTool({
            "success": False,
            "message": "Service status is inconclusive."
        }),
        "run_diagnostic": FakeTool({
            "success": True,
            "message": "Wi-Fi adapter was restarted."
        }),
        "verification": FakeTool({
            "success": True,
            "message": "Wi-Fi is working now."
        })
    }

    state = AgentState(
        original_goal="The Wi-Fi in Lab 3 isn't working.",
        location="Lab 3",
        issue_type="wifi"
    )

    agent = Agent(tools)

    result = agent.run(state)

    assert result.status == "RESOLVED"
    assert "check_service_status" in result.failed_steps
    assert "run_diagnostic" in result.completed_steps
    assert result.final_result == "Wi-Fi is working now."

def test_agent_stays_unresolved_when_all_tools_fail():

    tools = {
        "check_service_status": FakeTool({
            "success": False,
            "message": "Service status is inconclusive."
        }),
        "run_diagnostic": FakeTool({
            "success": False,
            "message": "Diagnostic could not fix the issue."
        }),
        "verification": FakeTool({
            "success": False,
            "message": "Wi-Fi is still not working."
        })
    }

    state = AgentState(
        original_goal="The Wi-Fi in Lab 3 isn't working.",
        location="Lab 3",
        issue_type="wifi"
    )

    agent = Agent(tools)

    result = agent.run(state)

    assert result.status != "RESOLVED"