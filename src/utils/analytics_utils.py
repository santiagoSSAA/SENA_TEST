from src.db import models
from sqlalchemy.orm import Session
from datetime import datetime

def log_transaction(db: Session, user_id: int, action: str, entity: str, entity_id: int, details: str = ""):
    # Placeholder: In real app, create a TransactionHistory model and save
    print(f"Transaction: {datetime.now()} | User {user_id} | {action} {entity} {entity_id} | {details}")
    # Example: db.add(models.TransactionHistory(...)); db.commit()
    return True

def get_transaction_history(db: Session, user_id: int = None):
    # Placeholder: In real app, query TransactionHistory model
    return [
        {"timestamp": str(datetime.now()), "user_id": user_id, "action": "CREATE", "entity": "Product", "entity_id": 1, "details": "Sample"}
    ]
