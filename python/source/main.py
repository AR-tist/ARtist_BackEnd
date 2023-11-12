### IMPORTS ###
from fastapi import FastAPI
import uvicorn
from routers import midi, root


### FastAPI ###
app = FastAPI()
app.include_router(root.router)
app.include_router(midi.router)


### MAIN ###
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)