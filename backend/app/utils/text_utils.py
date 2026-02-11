import re

def normalize_text(text: str) -> str:
    text = text.replace("’", "'")
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()