
import uvicorn
from fastapi import FastAPI
from app.api.ingestion import router as ingestion_router
from app.db.base import engine
from app.db.models import Base

# Initialize Database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MICRO_AFT Ingestion Layer")

# Include our modular routes
app.include_router(ingestion_router)

@app.get("/")
def health_check():
    return {"status": "online", "layer": "Data Ingestion & Integration"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
  
