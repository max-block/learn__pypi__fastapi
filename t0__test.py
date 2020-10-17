from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    data = await file.read()
    print("data", data)
    return "ok"
