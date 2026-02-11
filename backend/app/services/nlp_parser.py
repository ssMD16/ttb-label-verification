import re
from typing import Optional, Dict
from app.utils.text_utils import normalize_text

def extract_fields(text: str) -> Dict[str, Optional[str]]:
    cleaned = normalize_text(text)
    return {
        "brand": extract_brand(cleaned),
        "class_type": extract_class_type(cleaned),
        "abv": extract_abv(cleaned),
        "net_contents": extract_net_contents(cleaned),
        "warning": extract_warning(cleaned),
        "raw_text": cleaned,
    }

def extract_brand(text: str):
    lines = text.split("\n")
    for line in lines[:5]:
        if line.isupper() and 2 <= len(line.split()) <= 4:
            return line.strip()
    return None

CLASS_KEYWORDS = ["bourbon", "whiskey", "vodka", "gin", "rum", "wine", "beer"]

def extract_class_type(text: str):
    for line in text.split("\n"):
        if any(k in line.lower() for k in CLASS_KEYWORDS):
            return line.strip()
    return None

def extract_abv(text: str):
    m = re.search(r"(\d{1,2}\.?\d*)\s*%.*?(alc|alcohol)", text, re.I)
    return m.group(1) if m else None

def extract_net_contents(text: str):
    m = re.search(r"(\d+)\s*(ml|l|oz|fl oz)", text, re.I)
    return f"{m.group(1)} {m.group(2).upper()}" if m else None

def extract_warning(text: str):
    if "government warning" not in text.lower():
        return None
    start = text.lower().find("government warning")
    return text[start:]