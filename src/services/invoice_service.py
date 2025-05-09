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
    # Use only valid fields for the Invoice model
    valid_data = {key: value for key, value in invoice_data.__dict__.items() if not key.startswith('_')}
    invoice = models.Invoice(**valid_data)
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
