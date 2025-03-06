from fastapi import APIRouter, Response
from pathlib import Path

router = APIRouter(prefix='/media')

@router.get('/{pdf_name}')
def get_receipt(pdf_name: str):
    file_path = Path("media") / pdf_name

    with open(file_path, "rb") as f:
        return Response(content=f.read(), media_type="application/pdf")
