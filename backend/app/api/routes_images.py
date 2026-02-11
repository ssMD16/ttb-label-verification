from fastapi import APIRouter, UploadFile, File
from app.services.preprocessing import preprocess_image
from app.services.ocr_engine import run_ocr
from app.services.nlp_parser import extract_fields
from app.services.comparator import compare_fields
from app.models.response_models import VerificationResult

router = APIRouter()

DUMMY_EXPECTED = {
    "brand": "OLD TOM DISTILLERY",
    "class_type": "KENTUCKY STRAIGHT BOURBON WHISKEY",
    "abv": "45",
    "net_contents": "750 ML",
}

@router.post("/process", response_model=VerificationResult)
async def process_image(image: UploadFile = File(...)):
    raw = await image.read()
    processed = preprocess_image(raw)
    text = run_ocr(processed)
    parsed = extract_fields(text)
    result = compare_fields(parsed, DUMMY_EXPECTED)
    return VerificationResult(**result)