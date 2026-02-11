import zipfile
import uuid
import io
from fastapi.concurrency import run_in_threadpool
from app.services.preprocessing import preprocess_image
from app.services.ocr_engine import run_ocr
from app.services.nlp_parser import extract_fields
from app.services.comparator import compare_fields

JOB_RESULTS = {}
JOB_STATUS = {}

DUMMY_EXPECTED = {
    "brand": "OLD TOM DISTILLERY",
    "class_type": "KENTUCKY STRAIGHT BOURBON WHISKEY",
    "abv": "45",
    "net_contents": "750 ML",
}

async def process_zip_batch(zip_file):
    job_id = str(uuid.uuid4())
    JOB_RESULTS[job_id] = {}
    JOB_STATUS[job_id] = "processing"

    contents = await zip_file.read()
    z = zipfile.ZipFile(io.BytesIO(contents))

    for name in z.namelist():
        if name.lower().endswith((".png", ".jpg", ".jpeg")):
            img_bytes = z.read(name)
            run_in_threadpool(process_single_image, job_id, name, img_bytes)

    return job_id

def process_single_image(job_id, filename, img_bytes):
    processed = preprocess_image(img_bytes)
    text = run_ocr(processed)
    parsed = extract_fields(text)
    result = compare_fields(parsed, DUMMY_EXPECTED)
    JOB_RESULTS[job_id][filename] = result

def get_batch_status(job_id):
    return {
        "status": JOB_STATUS.get(job_id, "unknown"),
        "results": JOB_RESULTS.get(job_id, {}),
    }