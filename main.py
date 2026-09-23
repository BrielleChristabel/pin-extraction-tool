"""Module Name: REST API PIN Extraction Tool
   Description: Menghubungkan fungsi sanitasi PIN dengan framework FastAPI."""

from fastapi import FastAPI, HTTPException
import os
from pydantic import BaseModel
from app_v2_sanitized import process_text_to_pin
import uvicorn
# Inisialisasi Aplikasi FastAPI
app = FastAPI(title="PIN Extraction Tool", description="API For Extraction and PIN Sanitized", version="1.0.0")
# Skema Input Data 
class InputData(BaseModel):
    raw_text: str

class Textinput(BaseModel):
    raw_text: str
# Endpoint Utama (POST Request)
@app.post("/generate_pin")
def generate_pin(payload: InputData):
    try:
        pin_hasil = process_text_to_pin(payload.raw_text)
        return {"Status": "Sukses", "PIN": pin_hasil}
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    # mengambil port otomatis dari environment render
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)
