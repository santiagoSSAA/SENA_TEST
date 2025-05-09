from sqlalchemy.orm import Session
from src.db import models

def get_inventory(db: Session):
    return db.query(models.Inventory).all()
