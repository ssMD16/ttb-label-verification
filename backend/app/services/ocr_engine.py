import easyocr
import cv2
import numpy as np

# Initialize a single global EasyOCR reader in "lite" mode
# - English only
# - No GPU
# - Store models in /tmp to avoid bloating memory
reader = easyocr.Reader(
    ['en'],
    gpu=False,
    model_storage_directory="/tmp",
    download_enabled=True
)


def run_ocr(image_bytes: bytes) -> str:
    """
    Run OCR on raw image bytes and return extracted text as a single string.
    """
    if not image_bytes:
        return ""

    # Decode bytes into an OpenCV image
    arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    if img is None:
        return ""

    # Optional: basic grayscale + resize to keep memory usage low
    h, w = img.shape[:2]
    max_dim = 1200
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        img = cv2.resize(img, (int(w * scale), int(h * scale)))

    # Convert to grayscale for more stable OCR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Run EasyOCR
    results = reader.readtext(gray, detail=0, paragraph=False)

    # Join lines into a single text block
    return "\n".join(results)
