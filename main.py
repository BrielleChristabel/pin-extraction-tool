"""Module Name: REST API PIN Extraction Tool
   Description: Menghubungkan fungsi sanitasi PIN dengan framework FastAPI."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app_v2_sanitized import process_text_to_pin
# Inisialisasi Aplikasi FastAPI
app = FastAPI(title="Secure PIN Generator API")
# Skema Input Data 
class InputData(BaseModel):
    raw_text: str
# Endpoint Utama (POST Request)
@app.post("/generate_pin")
def generate_pin(payload: InputData):
    try: 
        pin_hasil = process_text_to_pin(payload.raw_text)
        return {"Status": "Sukses", "PIN": pin_hasil}
    except ("ValueError", "TypeError") as e:
        raise HTTPException(status_code=400, detail=str(e))