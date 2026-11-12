from typing import List

class FunctionCallingService:

    def __init__(self, function_definitions: List, decoder: str):
        self.function_definitions = function_definitions
        self.decoder = decoder
    
    def build_prompt(self, prompt: str):
        return f"answer the following prompt: [{prompt}] " \
               f"using the following functions: {self.function_definitions}"

    def call(self, prompt: str):
        full_prompt = self.build_prompt(prompt)
        self.decoder.generate(full_prompt)