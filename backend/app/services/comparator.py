from rapidfuzz import fuzz

OFFICIAL_WARNING = "GOVERNMENT WARNING: (1) ACCORDING TO THE SURGEON GENERAL..."

def compare_fields(parsed, expected):
    return {
        "brand_match": compare_brand(parsed["brand"], expected["brand"]),
        "class_type_match": parsed["class_type"] == expected["class_type"],
        "abv_match": parsed["abv"] == expected["abv"],
        "net_contents_match": parsed["net_contents"] == expected["net_contents"],
        "warning_match": parsed["warning"] == OFFICIAL_WARNING,
        "raw_text": parsed["raw_text"],
    }

def compare_brand(parsed, expected):
    if not parsed or not expected:
        return False
    return fuzz.ratio(parsed.lower(), expected.lower()) >= 85