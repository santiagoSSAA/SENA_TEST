from fastapi import BackgroundTasks
from src.utils.logger import logger
from src.services.notification_service import create_notification

def send_notification(message: str, user_id: int = None):
    # In real app, send email/SMS or in-app notification
    if user_id:
        logger.info(f"Notification sent to user {user_id}: {message}")
    else:
        logger.info(f"Notification sent to all users: {message}")
    return True

def trigger_alert(message: str, user_id: int = None, db=None):
    logger.warning(f"ALERT: {message}")
    if db and user_id:
        # Create a notification in the database for the user
        create_notification(db, schemas.NotificationCreate(message=message, user_id=user_id))
    elif db:
        # Notify all admins
        from src.db import models
        admins = db.query(models.User).filter(models.User.role == "admin").all()
        for admin in admins:
            create_notification(db, schemas.NotificationCreate(message=message, user_id=admin.id))
    return True
