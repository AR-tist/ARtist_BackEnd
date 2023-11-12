### IMPORTS ###
from fastapi import FastAPI
import uvicorn
from routers import midi, root
from fastapi.middleware.cors import CORSMiddleware

### FastAPI ###
app = FastAPI()
app.include_router(root.router)
app.include_router(midi.router)


### CORS ###
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

### MAIN ###
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)