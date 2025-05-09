from sqlalchemy.orm import Session
from src.db import models

def get_notifications(db: Session):
    return db.query(models.Notification).all()
