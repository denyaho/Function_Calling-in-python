from pydantic import BaseModel
from typing import Literal


class ParamDefinition(BaseModel):
    type: Literal["string", "number", "boolean", "array", "object"]


class ReturnDefinition(BaseModel):
    type: Literal["string", "number", "boolean", "array", "object"]


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: dict[str, ParamDefinition]
    returns: ReturnDefinition


class FunctionCall(BaseModel):
    prompt: str


class OutputFormat(BaseModel):
    prompt: str
    name: str
    parameters: dict[str, object]
