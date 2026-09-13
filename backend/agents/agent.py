from .state import AgentState
from .planner import Planner
from .evaluator import Evaluator
from .replanner import Replanner


class Agent:
    def __init__(self, tools):
        self.tools = tools
        self.planner = Planner()
        self.evaluator = Evaluator()
        self.replanner = Replanner()

    def run(self, state):
        while state.status not in ["RESOLVED", "ESCALATED", "FAILED"]:

            # Planning
            state.status = "PLANNING"

            if not state.next_action:
                state.next_action = self.planner.choose_action(state)

            action = state.next_action
            state.selected_action = action

            # No more actions available
            if action is None:
                state.status = "ESCALATED"
                state.final_result = (
                    "Unable to resolve automatically. Ticket required."
                )
                break

            # Check whether the required tool exists
            if action not in self.tools:
                state.failed_steps.append(action)
                state.status = "REPLANNING"

                next_action = self.replanner.choose_alternative(state)

                if next_action is None:
                    state.status = "ESCALATED"
                    state.final_result = (
                        "Unable to resolve automatically. Ticket required."
                    )
                    break

                state.next_action = next_action
                continue

            # Execute tool
            state.status = "EXECUTING"

            tool = self.tools[action]
            result = tool.execute(state)

            state.tool_results.append({
                "action": action,
                "result": result
            })

            # Evaluate result
            state.status = "EVALUATING"

            evaluation = self.evaluator.evaluate(result)

            if evaluation == "SUCCESS":
                state.completed_steps.append(action)

                # Successful execution moves to verification
                state.status = "VERIFYING"

                if "verification" in self.tools:
                    verification_result = self.tools["verification"].execute(state)

                    state.tool_results.append({
                        "action": "verification",
                        "result": verification_result
                    })

                    if verification_result.get("success") is True:
                        state.status = "RESOLVED"
                        state.final_result = verification_result.get(
                            "message",
                            "Issue resolved successfully."
                        )
                    else:
                        state.status = "REPLANNING"

                        next_action = self.replanner.choose_alternative(state)

                        if next_action is None:
                            state.status = "ESCALATED"
                            state.final_result = (
                                "Unable to resolve automatically. Ticket required."
                            )
                            break

                        state.next_action = next_action

                else:
                    state.status = "RESOLVED"
                    state.final_result = "Issue resolved successfully."

            else:
                state.failed_steps.append(action)
                state.status = "REPLANNING"

                next_action = self.replanner.choose_alternative(state)

                if next_action is None:
                    state.status = "ESCALATED"
                    state.final_result = (
                        "Unable to resolve automatically. Ticket required."
                    )
                    break

                state.next_action = next_action

        return state