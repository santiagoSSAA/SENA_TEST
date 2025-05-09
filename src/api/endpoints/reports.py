from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.utils.db_session import get_db
from src.services import report_service
from src.utils.security import get_current_user
from fpdf import FPDF
import pandas as pd
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/reports", response_model=dict)
def get_reports(period: str = None, warehouse: str = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return report_service.get_reports(db, period=period, warehouse=warehouse)

@router.get("/analytics", response_model=dict)
def get_analytics(group_by: str = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return report_service.get_analytics(db, group_by=group_by)

@router.get("/reports/export")
def export_reports(format: str = "excel", period: str = None, warehouse: str = None, product_id: int = None, user_id: int = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    data = report_service.get_reports(db, period=period, warehouse=warehouse, product_id=product_id, user_id=user_id)["report"]
    # For demo, data is a list of sale IDs; in real app, return full dicts
    rows = [{"sale_id": sid} for sid in data]
    if format == "pdf":
        return export_to_pdf(rows, filename="report.pdf")
    return export_to_excel(rows, filename="report.xlsx")

@router.get("/analytics/export")
def export_analytics(format: str = "excel", group_by: str = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    data = report_service.get_analytics(db, group_by=group_by)["analytics"]
    rows = [{"analytics": data}]
    if format == "pdf":
        return export_to_pdf(rows, filename="analytics.pdf")
    return export_to_excel(rows, filename="analytics.xlsx")

def export_to_pdf(data, filename="report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for row in data:
        line = ", ".join(f"{key}: {value}" for key, value in row.items())
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(filename)
    return FileResponse(filename, media_type="application/pdf", filename=filename)

def export_to_excel(data, filename="report.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    return FileResponse(filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=filename)
