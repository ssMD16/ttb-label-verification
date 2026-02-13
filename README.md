TTB Label Verification Prototype
================================

This project is a full‑stack prototype demonstrating automated label verification for alcohol beverage submissions.
It extracts text from product label images, parses key regulatory fields, and compares them against expected values.
The system supports both single‑image verification and batch ZIP processing.

This prototype was built as part of a technical assessment and is designed to be simple, transparent, and easy to run.


------------------------------------------------------------
FEATURES
------------------------------------------------------------

Single Label Verification
- Upload an image (JPG/PNG)
- OCR extracts text
- NLP parses:
  • Brand Name
  • Class/Type
  • ABV
  • Net Contents
  • Government Warning
- Results returned with match indicators

Batch ZIP Processing
- Upload a ZIP containing multiple label images
- Each image is processed asynchronously
- Poll for job status
- Results returned per file

Frontend (React + Vite)
- Simple UI for uploading images and ZIP files
- Displays parsed fields and match results
- Communicates with backend via REST API

Backend (FastAPI)
- OCR (EasyOCR or Tesseract)
- Image preprocessing (OpenCV)
- NLP parsing
- Fuzzy matching (RapidFuzz)
- Batch job manager (in‑memory)


------------------------------------------------------------
ARCHITECTURE OVERVIEW
------------------------------------------------------------

frontend/        → React + Vite UI
backend/         → FastAPI application
  app/
    api/         → API routes (image + batch)
    services/    → OCR, NLP, preprocessing, comparison
    models/      → Request/response schemas
    utils/       → Helpers


------------------------------------------------------------
TECH STACK
------------------------------------------------------------

Frontend:
- React 18
- Vite
- Fetch API

Backend:
- FastAPI
- Uvicorn
- EasyOCR or Tesseract OCR
- OpenCV
- RapidFuzz
- Pydantic / Pydantic‑Settings


------------------------------------------------------------
INSTALLATION & LOCAL DEVELOPMENT
------------------------------------------------------------

1. Clone the repository:

    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>


------------------------------------------------------------
BACKEND SETUP (FASTAPI)
------------------------------------------------------------

Install dependencies:

    cd backend
    pip install -r requirements.txt

Run the server:

    uvicorn app.main:app --reload

Backend will be available at:
    http://localhost:8000

Interactive API docs:
    http://localhost:8000/docs


------------------------------------------------------------
FRONTEND SETUP (REACT + VITE)
------------------------------------------------------------

Install dependencies:

    cd frontend
    npm install

Run the development server:

    npm run dev

Frontend will be available at:
    http://localhost:5173


------------------------------------------------------------
CONNECTING FRONTEND TO BACKEND
------------------------------------------------------------

Edit:

    frontend/src/config.js

Set:

    export const API_BASE_URL = "http://localhost:8000";

For production, replace with your Render backend URL.


------------------------------------------------------------
DEPLOYMENT
------------------------------------------------------------

Backend (Render)
----------------
1. Create a new Web Service
2. Connect GitHub repo
3. Set Root Directory to: backend
4. Build Command:
       pip install -r requirements.txt
5. Start Command:
       uvicorn app.main:app --host 0.0.0.0 --port 10000
6. Deploy


Frontend (Netlify)
------------------
1. Create new site → Import from Git
2. Set Base Directory:
       frontend
3. Build Command:
       npm run build
4. Publish Directory:
       dist
5. Deploy
6. Update API_BASE_URL to your Render backend URL


------------------------------------------------------------
API USAGE
------------------------------------------------------------

Single Image:
    POST /image/process
    FormData:
      image: <file>

Batch ZIP:
    POST /batch/process
    FormData:
      zip_file: <zip>

Poll Batch Status:
    GET /batch/status/{job_id}


------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------

backend/
  app/
    main.py
    api/
      routes_images.py
      routes_batch.py
    services/
      preprocessing.py
      ocr_engine.py
      nlp_parser.py
      comparator.py
      batch_manager.py
    models/
      response_models.py
    utils/
      text_utils.py

frontend/
  index.html
  package.json
  vite.config.js
  src/
    App.jsx
    main.jsx
    config.js


------------------------------------------------------------
NOTES & LIMITATIONS
------------------------------------------------------------

- OCR accuracy varies depending on image quality
- Batch processing uses in‑memory storage (not persistent)
- Expected values are hardcoded for demonstration
- This is a prototype, not a production system

