from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.db import models
from src.utils.security import hash_password

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user_data):
    user = models.User(
        username=user_data.username,
        hashed_password=hash_password(user_data.password),
        role=getattr(user_data, "role", "user")
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db, user_id):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(db, user_id, user_data):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_data.dict().items():
        if key == "password":
            user.hashed_password = hash_password(value)
        elif key != "password":
            setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db, user_id):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
