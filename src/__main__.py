from src.loader import load_function_definitions, load_prompts
import argparse
from pathlib import Path
import sys
from llm_sdk import Small_LLM_Model
from src.LLMClient import LLMClient 
from src.FunctionCalling import FunctionCallingService
from src.ConstrainedDecoding import ConstrainedDecoding

INPUT_DIR = "data/input"
OUTPUT_DIR = "data/output"
FUNCTIONS_DEFINITION = "functions_definition.json"
INPUT_FILE = "function_calling_tests.json"
OUTPUT_FILE = "function_calling_results.json"

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Load and print function definitions from a JSON file.")
    parser.add_argument("--functions_definition", type=Path,
                            default=Path(INPUT_DIR + "/" + FUNCTIONS_DEFINITION))
    parser.add_argument("--input", type=Path,
                            default=Path(INPUT_DIR + "/" + INPUT_FILE))
    parser.add_argument("--output", type=Path,
                            default=Path(OUTPUT_DIR + "/" + OUTPUT_FILE))
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Unknown arguments: {unknown}")
        sys.exit(2)
    return args

def main():
    args = parse_args()

    functions_path = str(args.functions_definition)
    prompt_path = str(args.input)
    output_path = str(args.output)

    function_definitions = load_function_definitions(functions_path)
    prompts = load_prompts(prompt_path)

    model = Small_LLM_Model()
    llm = LLMClient(model)
    decoder = ConstrainedDecoding(llm, function_definitions)
    service = FunctionCallingService(function_definitions, decoder)
    for prompt in prompts:
        service.call(prompt)



if __name__ == "__main__":
    main()