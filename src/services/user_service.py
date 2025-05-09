from sqlalchemy.orm import Session
from src.db import models

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user_data):
    user = models.User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
