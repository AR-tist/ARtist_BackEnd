from fastapi import APIRouter, UploadFile, File, Form
from pymongo import MongoClient
from fastapi.responses import JSONResponse
import os
import datetime

router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)

client = MongoClient('mongodb://localhost:27017/')
db = client['artist']
collection = db['MidiFile']

@router.post("/")
async def upload_midi_file(
    title: str = Form(...),
    subtitle: str = Form(...),
    poster: str = Form(...),
    file: UploadFile = File(...),
):
    # 미디 파일이 아닌 경우 에러 응답
    if not file.filename.endswith(".mid"):
        return JSONResponse(content={"error": "Invalid file format"}, status_code=400)

    # 파일 저장 경로 설정
    date_suffix = datetime.datetime.now().timestamp()
    file_path = os.path.join("/home/ubuntu/upload", f"{title}-{date_suffix}.mid")

    # 파일 저장
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # MongoDB에 데이터 저장
    new_midi_file = {
        "filename": file_path,
        "title": title,
        "imgurl": "",
        "subtitle": subtitle,
        "poster": poster,
        "rank": 0,
        "like": 0,
        "views": 0,
        "music_length": 0,
        "timestamp": date_suffix,
    }
    output = collection.insert_one(new_midi_file)
    print(output.inserted_id)

    # 응답 생성
    response = {
        "timestamp": date_suffix,
        "filename": file_path,
        "title": title,
        "downloadUrl": f"/download/{output.inserted_id}",
    }

    return response
