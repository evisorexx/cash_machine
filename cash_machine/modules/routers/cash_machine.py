from fastapi import APIRouter, HTTPException, Response
from collections import Counter
from datetime import datetime
from cash_machine.config import BASE_URL
from ..models.items import Item
from ..schemas.items import ItemSchema, ItemRequestSchema
from ...common import generate_pdf, generate_qr
from ...common.database import test_db_setup
from ...services import render_receipt


router = APIRouter(prefix='/cash_machine')
# db = Database() - через эндпоинт add_items можно добавлять свои товары для проверки.
db = test_db_setup()


@router.post('/')
def generate_receipt(request: ItemRequestSchema):
    item_ids = request.items

    item_counter = Counter(item_ids)
    items_in_receipt = []

    for item_id, quantity in item_counter.items():
        try:
            item = db.get_item_by_id(item_id)
            items_in_receipt.append({
                'title': item.title,
                'quantity': quantity,
                'total': round(item.price * quantity, 2)
            })
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
