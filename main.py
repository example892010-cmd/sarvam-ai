import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online", "message": "Sarvam AI service is running successfully!"}

@app.get("/health")
def health_check():
    return {"health": "ok"}

if __name__ == "__main__":
    import uvicorn
    # Render assigns a dynamic port via the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
