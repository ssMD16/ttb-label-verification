import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def run_ocr(image):
    if image is None:
        return ""
    results = reader.readtext(image, detail=0)
    return "\n".join(results)