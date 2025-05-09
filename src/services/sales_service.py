from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.db import models
from src.services.transaction_service import log_transaction

def get_sales(db: Session):
    return db.query(models.Sale).all()

def create_sale(db: Session, sale_data):
    sale = models.Sale(**sale_data)
    db.add(sale)
    db.commit()
    db.refresh(sale)
    # Log transaction
    log_transaction(db, sale.user_id, "CREATE", "Sale", sale.id, details="Sale created")
    # Auto-generate invoice after sale
    from src.services.invoice_service import create_invoice
    invoice_data = models.Invoice(sale_id=sale.id, total=sale.total)
    create_invoice(db, invoice_data)
    return sale

def get_sale(db, sale_id):
    sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

def update_sale(db, sale_id, sale_data):
    sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    for key, value in sale_data.dict().items():
        setattr(sale, key, value)
    db.commit()
    db.refresh(sale)
    return sale

def delete_sale(db, sale_id):
    sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    db.delete(sale)
    db.commit()
