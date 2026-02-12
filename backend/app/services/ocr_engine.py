import easyocr

# Load only English, disable GPU, disable unnecessary detection models
reader = easyocr.Reader(
    ['en'], 
    gpu=False,
    model_storage_directory="/tmp",  # prevents caching large models in memory
    download_enabled=True
)

def run_ocr(image):
    if image is None:
        return ""
    results = reader.readtext(image, detail=0, paragraph=False)
    return "\n".join(results)
