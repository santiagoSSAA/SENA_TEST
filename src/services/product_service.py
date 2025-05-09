from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.db import models

def get_products(db: Session):
    return db.query(models.Product).all()

def create_product(db: Session, product_data):
    product = models.Product(**product_data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product(db, product_id):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def update_product(db, product_id, product_data):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product_data.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db, product_id):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()

# Similar CRUD for users, sales, inventory, etc. (expand as needed)
