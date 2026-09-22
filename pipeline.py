from llm_sdk import Small_LLM_Model
from src.loader import FunctionDefinition, load_prompts, load_function_definitions


class FunctionCaller:
    def __init__(self: "FunctionCaller", definition: list[FunctionDefinition]):
        self.model = Small_LLM_Model()
        self.definition = definition

    def add_definition(self, prompt: FunctionDefinition):
        new_prompts = (
            "Answer this "
            + str(prompt)
            + " based on these function definition"
            + str(self.definition)
        )
        return new_prompts
    
    def run():


def run_pipeline(input_path: str, functions_path: str):
    prompts = load_prompts(input_path)
    definition = load_function_definitions(functions_path)
    caller = FunctionCaller(definition)
