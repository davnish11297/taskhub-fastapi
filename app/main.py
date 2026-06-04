from fileinput import filename
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.db.database import Base, engine
from app.s3_client import upload_file, list_files, download_file
import traceback

from app.models import User, Task
from app.routes import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskHub AWS Project")

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "TaskHub API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        content = await file.read()
        result = upload_file(file.filename, content)
        return {"message": "uploaded", "data": result}
    except Exception as e:
        print("ERROR OCCURED:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/files")
def files():
    return list_files()

@app.get(f"/download/{filename}")
def download(filename: str):
    content = download_file(filename)
    return {"file": filename, "content": content.decode("utf-8", errors="ignore")}