class Replanner:
    def choose_alternative(self, state):
        print("FAILED STEPS:", state.failed_steps)

        failed_actions = set(state.failed_steps)

        possible_actions = [
            "check_service_status",
            "run_diagnostic",
            "check_knowledge_base",
            "create_ticket"
        ]

        for action in possible_actions:
            if action not in failed_actions:
                print("REPLANNER CHOSE:", action)
                return action

        print("REPLANNER: NO ACTION LEFT")
        return None