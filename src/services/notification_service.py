from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.db import models

def get_notifications(db: Session):
    return db.query(models.Notification).all()

def get_notification(db: Session, notification_id: int):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

def create_notification(db: Session, notification_data: models.Notification):
    notification = models.Notification(**notification_data.dict())
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification

def delete_notification(db: Session, notification_id: int):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(notification)
    db.commit()
