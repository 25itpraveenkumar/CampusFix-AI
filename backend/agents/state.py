from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentState:
    original_goal: str
    location: str = ""
    issue_type: str = ""

    current_step: str = ""
    completed_steps: list[str] = field(default_factory=list)
    failed_steps: list[str] = field(default_factory=list)

    tool_results: list[dict[str, Any]] = field(default_factory=list)

    selected_action: str = ""
    next_action: str | None = None

    status: str = "PLANNING"
    final_result: str = ""