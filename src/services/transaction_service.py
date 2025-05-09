from sqlalchemy.orm import Session
from src.db import models

def log_transaction(db: Session, user_id: int, action: str, entity: str, entity_id: int, details: str = ""):
    tx = models.TransactionHistory(
        user_id=user_id,
        action=action,
        entity=entity,
        entity_id=entity_id,
        details=details
    )
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def get_transaction_history(db: Session, user_id: int = None):
    query = db.query(models.TransactionHistory)
    if user_id:
        query = query.filter(models.TransactionHistory.user_id == user_id)
    return query.order_by(models.TransactionHistory.timestamp.desc()).all()
