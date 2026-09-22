from src.loader import load_function_definitions, load_prompts
import argparse
from pipeline import run_pipeline
from pathlib import Path
import sys

INPUT_DIR = "data/input"
OUTPUT_DIR = "data/output"
FUNCTIONS_DEFINITION = "functions_definition.json"
INPUT_FILE = "function_calling_tests.json"
OUTPUT_FILE = "function_calling_results.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Load and print function definitions from a JSON file."
    )
    parser.add_argument(
        "-functions_definition", type=Path, default=Path(FUNCTIONS_DEFINITION)
    )
    parser.add_argument("-input", type=Path, default=Path(INPUT_FILE))
    parser.add_argument("-output", type=Path, default=Path(OUTPUT_FILE))
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Unknown arguments: {unknown}")
        sys.exit(2)
    return args


if __name__ == "__main__":
    args = parse_args()

    functions_path = INPUT_DIR + "/" + args.functions_definition.name
    input_path = INPUT_DIR + "/" + args.input.name
    output_path = OUTPUT_DIR + "/" + args.output.name

    function_definitions = load_function_definitions(functions_path)
    run_pipeline(input_path)
