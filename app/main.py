from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AgenticHub-AI")

app.include_router(router)

@app.get("/health")
def health():
    return {"Status": "OK"}