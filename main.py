from fastapi import FastAPI, UploadFile, File
from rag_chain import suggest_infrastructure_projects
import shutil

app = FastAPI()

@app.post("/upload/doc")
async def upload_doc(file: UploadFile = File(...)):
    with open(f"data/documents/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": f"Document {file.filename} uploaded."}

@app.post("/upload/geo")
async def upload_geo(file: UploadFile = File(...)):
    with open(f"data/geodata/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": f"Geo file {file.filename} uploaded."}

@app.get("/generate")
def generate():
    return suggest_infrastructure_projects()