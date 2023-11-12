### IMPORTS ###
from fastapi import FastAPI
import uvicorn
from routers import item, root


### FastAPI ###
app = FastAPI()
app.include_router(item.router)
app.include_router(root.router)


### MAIN ###
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)