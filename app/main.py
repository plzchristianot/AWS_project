from fastapi import FastAPI, APIRouter
from app.routers.api_router import router

app = FastAPI(title="AWS project")

app.include_router(router)

@app.get("/")
async def root():
    return "hey!"