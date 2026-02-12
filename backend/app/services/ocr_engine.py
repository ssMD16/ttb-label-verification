import pytesseract
import cv2
import numpy as np

def run_ocr(image):
    if image is None:
        return ""
    return pytesseract.image_to_string(image)
