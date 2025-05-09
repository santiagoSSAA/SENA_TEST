from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.db_session import get_db
from src.services import notification_service
from src.db import schemas
from src.utils.security import get_current_user, require_role

router = APIRouter()

@router.get("/notifications", response_model=List[schemas.NotificationOut])
def list_notifications(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return notification_service.get_notifications(db)

@router.get("/notifications/{notification_id}", response_model=schemas.NotificationOut)
def get_notification(notification_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return notification_service.get_notification(db, notification_id)

@router.post("/notifications", response_model=schemas.NotificationOut, status_code=status.HTTP_201_CREATED)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return notification_service.create_notification(db, notification)

@router.delete("/notifications/{notification_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_notification(notification_id: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    notification_service.delete_notification(db, notification_id)
    return None
