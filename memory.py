import BaseModel from pydantic
from typing import Literal

class Fact(BaseModel):
    category: Literal ["account", "preference"]
    key: str
    value: str
    statement: str
    evidence_quote: str
