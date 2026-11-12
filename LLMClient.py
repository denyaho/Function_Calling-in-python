from typing import List

class LLMClient:
    def __init__(self, model):
        self.model = model

    def get_vocab(self) -> dict:
        vocab_path = self.model.get_path_to_vocab_file()

        import json
        with open(vocab_path, "r") as f:
            vocab = json.load(f)
        return vocab

    def encode(self, prompt: str) -> List[int]:
        inputs = self.model.encode(prompt)
        return inputs[0].tolist()
    