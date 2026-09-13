class Evaluator:
    def evaluate(self, tool_result):
        if tool_result.get("success") is True:
            return "SUCCESS"

        if tool_result.get("success") is False:
            return "FAILURE"

        return "INSUFFICIENT"