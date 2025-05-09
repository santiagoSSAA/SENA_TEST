from sqlalchemy.orm import Session
from src.db import models

def get_products(db: Session):
    return db.query(models.Product).all()

def create_product(db: Session, product_data):
    product = models.Product(**product_data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Similar CRUD for users, sales, inventory, etc. (expand as needed)
