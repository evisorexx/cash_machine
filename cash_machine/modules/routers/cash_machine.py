from fastapi import APIRouter, HTTPException, Response
from datetime import datetime
from cash_machine.config import BASE_URL, db
from ..models.items import Item
from ..schemas.items import ItemSchema, ItemRequestSchema
from ...common import generate_pdf, generate_qr
from ...services import render_receipt, generate_receipt_values


router = APIRouter(prefix='/cash_machine')
# db = Database() - таким образом через эндпоинт add_items можно добавлять свои товары для проверки.


@router.post('/')
def generate_receipt(request: ItemRequestSchema):
    item_ids = request.items
    try:
        items_in_receipt = generate_receipt_values(item_ids)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    receipt_data = {
        'items': items_in_receipt,
        'total': sum(item['total'] for item in items_in_receipt),
        'created_at': datetime.now().strftime('%d.%m.%Y %H:%M')
    }

    html_receipt = render_receipt(receipt_data)

    try:
        pdf_path = generate_pdf(html_receipt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    full_url = f'{BASE_URL}/{pdf_path}'

    try:
        qr_image_bytes = generate_qr(full_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Failed to generate QR code: {str(e)}')

    return Response(content=qr_image_bytes, media_type='image/png')


@router.post('/add_item')  # dev-endpoint
def add_item(item: ItemSchema):
    new_item = Item(id=item.id, title=item.title, price=item.price)
    db.add_item(new_item)
    return {'message': 'Item added successfully'}
