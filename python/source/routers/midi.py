from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from fastapi.responses import JSONResponse
import os
import datetime

router = APIRouter(
    prefix="/midi",
    tags=["midi"]
)

client = MongoClient('mongodb://localhost:27017/')
db = client['artist']
collection = db['MidiFile']

@router.get("/list")
async def get_midi_list():
    try:
        # MongoDB에서 데이터 가져오기
        files = collection.find({}, projection={"_id": False, "filename": True, "timestamp": True, "title": True, "imgurl": True, "subtitle": True, "rank": True, "poster": True, "like": True, "views": True, "music_length": True})

        # 가져온 데이터를 JSON 형식으로 변환
        file_list = []
        for file in files:
            download_url = f"/download/{file['filename']}"
            delete_url = f"/delete/{file['filename']}"
            file_item = {
                "timestamp": file["timestamp"],
                "filename": file["filename"],
                "title": file["title"],
                "imgurl": file["imgurl"],
                "subtitle": file["subtitle"],
                "rank": file["rank"],
                "poster": file["poster"],
                "like": file["like"],
                "views": file["views"],
                "music_length": file["music_length"],
                "downloadUrl": download_url,
                "deleteUrl": delete_url,
            }
            file_list.append(file_item)

        # JSON 응답 반환
        return JSONResponse(content=jsonable_encoder(file_list))
    except Exception as e:
        # 에러 발생 시 500 에러 응답
        raise HTTPException(status_code=500, detail="Error retrieving MIDI file list")
        

@router.post("/upload")
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
