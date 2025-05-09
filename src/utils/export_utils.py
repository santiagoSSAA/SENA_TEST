from fastapi import HTTPException
from pydantic import BaseModel
from typing import Any
import io
from starlette.responses import StreamingResponse
import pandas as pd
from fpdf import FPDF

def export_to_excel(data: list[dict[str, Any]], filename: str = "export.xlsx"):
    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={"Content-Disposition": f"attachment; filename={filename}"})

def export_to_pdf(data: list[dict[str, Any]], filename: str = "export.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for row in data:
        pdf.cell(200, 10, txt=str(row), ln=True)
    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)
    return StreamingResponse(output, media_type='application/pdf', headers={"Content-Disposition": f"attachment; filename={filename}"})
