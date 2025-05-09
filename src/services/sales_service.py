from sqlalchemy.orm import Session
from src.db import models

def get_sales(db: Session):
    return db.query(models.Sale).all()

def create_sale(db: Session, sale_data):
    sale = models.Sale(**sale_data)
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale
