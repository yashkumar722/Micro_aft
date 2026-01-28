from fastapi import FastAPI
from app.db.base import engine # Assuming you've created db/base.py
from app.db.models import Base

# Create tables automatically on start
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MICRO_AFT")

@app.get("/")
def read_root():
    return {"status": "MICRO_AFT Layer 1 is Online"}
  
