import json
from src.models import FunctionDefinition, ParamDefinition, ReturnDefinition
from pydantic import ValidationError

def load_function_calling(filename: str):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        prompts = []
        for item in data:
            prompts.append(
                ParamDefinition(type = item["parameters"]["type"])
            )
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 
    except json.JSONDecodeError:
        print(f"{filename} is not a valid JSON file.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    return prompts


def load_function_definitions(filename: str) -> list[FunctionDefinition]:
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        functions = []
        for item in data:
            functions.append(
                FunctionDefinition(
                    name = item["name"],
                    description = item["description"],
                    parameters = {k: ParamDefinition(type = v["type"]) for k, v in item["parameters"].items()},
                    returns = ReturnDefinition(type = item["returns"]["type"])
                )
            )
        print(functions)
    except ValidationError as e:
        print(f"Validation error: {e}")
        return
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 
    except json.JSONDecodeError:
        print(f"{filename} is not a valid JSON file.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    return functions

