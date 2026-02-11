from pydantic import BaseModel
from typing import Any, Dict

class VerificationResult(BaseModel):
    brand_match: Any
    class_type_match: Any
    abv_match: Any
    net_contents_match: Any
    warning_match: Any
    raw_text: str