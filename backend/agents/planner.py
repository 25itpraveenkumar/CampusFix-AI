class Planner:
    def choose_action(self, state):
        if state.issue_type == "wifi":
            return "check_service_status"

        if state.issue_type == "projector":
            return "check_knowledge_base"

        if state.issue_type == "printer":
            return "check_service_status"

        return "check_knowledge_base"