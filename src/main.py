#!/usr/bin/env python3

from llm_sdk import Small_LLM_Model
import numpy as np
from loader import load_function_definitions

def force_token(logits: list, forced_token_id: int):
    return [logit if i == forced_token_id else -np.inf for i, logit in enumerate(logits)]
    
if __name__ == "__main__":
    function_definitions = load_function_definitions("../data/input/functions_definitions.json")
    print(function_definitions)
    # model = Small_LLM_Model()

    
    # vocab_path = model.get_path_to_vocab_file()
    # print(f"Path to vocab file: {vocab_path}")

    # import json
    # with open(vocab_path, "r") as f:
    #     vocab = json.load(f)
    # print(f"Vocab size: {len(vocab)}")
    # print(f"First 100 vocab entries: {list(vocab.items())[:100]}")

    # brackets = ["(", ")", "{", "}", "[", "]"]
    # forced_token_id = vocab["("]
    # for key, value in vocab.items():
    #     if key in brackets:
    #         print(f"Bracket token: {key} -> {value}")

    # input_ids = model.encode("Hello, world!, introduce yourself")
    # print(f"Input IDs: {input_ids}")

    # max_new_tokens = 10

    # input_ids_list = input_ids[0].tolist()

    # for _ in range(max_new_tokens):
    #     logits = model.get_logits_from_input_ids(input_ids_list)
    #     masked_logits = force_token(logits, forced_token_id)
    #     next_token_id = int(np.argmax(masked_logits))
    #     input_ids_list.append(next_token_id)
    # print(model.decode(input_ids_list))

