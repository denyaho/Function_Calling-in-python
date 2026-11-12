
class ConstrainedDecoding:
    def __init__(self, llm, function_definitions):
        self.model = llm
        self.function_definitions = function_definitions

    def generate(self):
