from sqlalchemy.orm import Session
from src.db import models

def get_invoices(db: Session):
    return db.query(models.Invoice).all()
