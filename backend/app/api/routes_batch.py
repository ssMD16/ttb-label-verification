from fastapi import APIRouter, UploadFile, File
from app.services.batch_manager import process_zip_batch, get_batch_status

router = APIRouter()

@router.post("/process")
async def process_batch(zip_file: UploadFile = File(...)):
    job_id = await process_zip_batch(zip_file)
    return {"job_id": job_id}

@router.get("/status/{job_id}")
async def batch_status(job_id: str):
    return get_batch_status(job_id)