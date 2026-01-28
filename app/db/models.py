from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class RawIngestion(Base):
    __tablename__ = "raw_ingestion"
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, nullable=False)
    batch_id = Column(String, index=True)
    payload = Column(JSON)
    metadata_info = Column(JSON)
    ingested_at = Column(DateTime, server_default=func.now())
  
