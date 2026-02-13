import pytesseract
import cv2
import numpy as np

def run_ocr(image_bytes: bytes) -> str:
    if not image_bytes:
        return ""

    arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    if img is None:
        return ""

    # Resize large images to reduce memory usage
    h, w = img.shape[:2]
    max_dim = 1200
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        img = cv2.resize(img, (int(w * scale), int(h * scale)))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Run Tesseract
    text = pytesseract.image_to_string(gray)

    return text.strip()
