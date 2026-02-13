from paddleocr import PaddleOCR
import cv2
import numpy as np

# Initialize lightweight OCR model
ocr = PaddleOCR(
    use_angle_cls=False,
    lang='en',
    use_gpu=False
)

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

    # Run OCR
    result = ocr.ocr(img, cls=False)

    # Extract text lines
    lines = []
    for block in result:
        for line in block:
            lines.append(line[1][0])

    return "\n".join(lines)
