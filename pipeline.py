from llm_sdk import Small_LLM_Model
from src.loader import FunctionDefinition

class FunctionCaller:
    def __init__(self, definition: list[FunctionDefinition]):
        self.model = Small_LLM_Model()
        self.definition = definition
    