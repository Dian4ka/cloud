import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Render!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Отримує порт із змінних середовища
    uvicorn.run(app, host="0.0.0.0", port=port)
