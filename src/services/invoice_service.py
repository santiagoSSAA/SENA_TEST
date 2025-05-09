from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.db import models

def get_invoices(db: Session):
    return db.query(models.Invoice).all()

def get_invoice(db: Session, invoice_id: int):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

def create_invoice(db: Session, invoice_data: models.Invoice):
    invoice = models.Invoice(**invoice_data.dict())
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice

def delete_invoice(db: Session, invoice_id: int):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    db.delete(invoice)
    db.commit()
