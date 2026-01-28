import uuid
from sqlalchemy.orm import Session
from app.db.models import RawIngestion

class IngestionManager:
    def __init__(self, db: Session):
        self.db = db

    async def process_ingestion(self, source_id, raw_content, connector):
        data_list = connector.transform_to_standard_json(raw_content)
        batch_id = str(uuid.uuid4())
        
        db_objects = [
            RawIngestion(
                source_id=source_id,
                batch_id=batch_id,
                payload=record,
                metadata_info={"origin": "manual_upload"}
            ) for record in data_list
        ]
        self.db.bulk_save_objects(db_objects)
        self.db.commit()
        return batch_id
      
