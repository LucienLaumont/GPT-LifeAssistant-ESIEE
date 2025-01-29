from fastapi import FastAPI
from api.routes.llm_router import router as llm_router

app = FastAPI()

app.include_router(llm_router, prefix="/api")


