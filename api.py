from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from src.chatterbox.tts import tts_function  # Placeholder, replace with actual import
from src.chatterbox.vc import vc_function    # Placeholder, replace with actual import
import io

app = FastAPI(title="Chatterbox TTS & VC API")

@app.post("/tts")
def tts_endpoint(text: str = Form(...)):
    """Text-to-Speech endpoint. Returns audio for input text."""
    # Replace with actual TTS logic
    audio_bytes = tts_function(text)  # Should return bytes or BytesIO
    return StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/wav")

@app.post("/vc")
def vc_endpoint(file: UploadFile = File(...), speaker_id: str = Form(...)):
    """Voice Conversion endpoint. Returns converted audio."""
    # Replace with actual VC logic
    input_audio = file.file.read()
    audio_bytes = vc_function(input_audio, speaker_id)  # Should return bytes or BytesIO
    return StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/wav")

@app.get("/")
def root():
    return JSONResponse({"message": "Chatterbox TTS & VC API is running."})
