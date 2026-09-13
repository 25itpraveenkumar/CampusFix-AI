from fastapi import APIRouter
from pydantic import BaseModel

from backend.agents.agent import Agent
from backend.agents.state import AgentState

from backend.tools.service_status import get_service_status
from backend.tools.diagnostic import run_diagnostic
from backend.tools.knowledge import get_knowledge
from backend.tools.ticket import create_ticket
from backend.tools.verification import verify_issue


router = APIRouter(prefix="/api")


class ToolAdapter:
    """Connect existing tool functions to the Agent."""

    def __init__(self, function, name):
        self.function = function
        self.name = name

    def execute(self, state):
        if self.name == "check_service_status":
            return self.function(state.issue_type)

        if self.name == "run_diagnostic":
            return self.function(
                check="connectivity_check",
                location=state.location,
                attempt=2,
            )

        if self.name == "check_knowledge_base":
            return self.function(
                issue=state.issue_type,
                location=state.location,
            )

        if self.name == "create_ticket":
            return self.function(
                location=state.location,
                issue=state.issue_type,
                priority="high",
                description=state.original_goal,
            )

        if self.name == "verification":
            return self.function(
                issue=state.issue_type,
                location=state.location,
                action_completed=True,
            )

        return {
            "success": False,
            "message": f"Unknown tool: {self.name}",
        }


class SolveRequest(BaseModel):
    issue: str
    location: str


def build_tools():
    return {
        "check_service_status": ToolAdapter(
            get_service_status,
            "check_service_status",
        ),
        "run_diagnostic": ToolAdapter(
            run_diagnostic,
            "run_diagnostic",
        ),
        "check_knowledge_base": ToolAdapter(
            get_knowledge,
            "check_knowledge_base",
        ),
        "create_ticket": ToolAdapter(
            create_ticket,
            "create_ticket",
        ),
        "verification": ToolAdapter(
            verify_issue,
            "verification",
        ),
    }


@router.post("/solve")
def solve_issue(request: SolveRequest):

    state = AgentState(
        original_goal=request.issue,
        location=request.location,
        issue_type=request.issue.lower(),
    )

    tools = build_tools()

    agent = Agent(tools)

    final_state = agent.run(state)

    return {
        "success": final_state.status == "RESOLVED",
        "status": final_state.status,
        "message": final_state.final_result,
        "data": {
            "issue": request.issue,
            "location": request.location,
            "completed_steps": final_state.completed_steps,
            "failed_steps": final_state.failed_steps,
            "tool_results": final_state.tool_results,
        },
    }