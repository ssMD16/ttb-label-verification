from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.api.routes_images import router as image_router
from app.api.routes_batch import router as batch_router

setup_logging()

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_router, prefix="/image", tags=["Image Processing"])
app.include_router(batch_router, prefix="/batch", tags=["Batch Processing"])

@app.get("/")
def root():
    return {"message": "Backend running"}