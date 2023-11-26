from fastapi import FastAPI
from core_service import service as core_service

app = FastAPI()
app.include_router(core_service.core_service)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
