from fastapi import FastAPI
from src.api.endpoints import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "SENA_TEST backend is running!"}
