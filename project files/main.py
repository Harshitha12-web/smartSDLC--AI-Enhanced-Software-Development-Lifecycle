from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from smart_sdlc import smart_sdlc_pipeline

app = FastAPI()

# Enable CORS so React frontend can call FastAPI backend (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter setup
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from the React build directory
app.mount("/static", StaticFiles(directory="build/static"), name="static")

# Serve the React index.html as root route
@app.get("/")
def serve_react_index():
    return FileResponse("build/index.html")

# API endpoint to run Smart SDLC pipeline
@app.get("/run_pipeline")
def run_pipeline(project: str = "Build a student attendance system"):
    return smart_sdlc_pipeline(project)
