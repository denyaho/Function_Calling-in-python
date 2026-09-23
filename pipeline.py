from llm_sdk import Small_LLM_Model
from src.loader import FunctionDefinition, load_prompts, load_function_definitions, FunctionCall


class FunctionCaller:
    def __init__(self: "FunctionCaller", definition: list[FunctionDefinition]):
        self.model = Small_LLM_Model()
        self.definition = definition

    def add_definition(self, prompt: FunctionDefinition) -> str:
        new_prompts = (
            str(prompt)
            + " Answer this question using this function definition"
            + str(self.definition)
        )
        return new_prompts        

    def constrained(self):

    
    def run(self, prompts: list[FunctionCall]):
        for prompt in prompts:
            added_prompt = self.add_definition(prompt)
            input_ids = self.model.encode(added_prompt)


def run_pipeline(input_path: str, functions_path: str):
    prompts = load_prompts(input_path)
    definition = load_function_definitions(functions_path)
    caller = FunctionCaller(definition)
    caller.run(prompts)