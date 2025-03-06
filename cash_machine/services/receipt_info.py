from collections import Counter
from ..config import db


def generate_receipt_values(item_ids: list):
    items_in_receipt = []
    item_counter = Counter(item_ids)
    for item_id, quantity in item_counter.items():
        item = db.get_item_by_id(item_id)
        items_in_receipt.append({
            'title': item.title,
            'quantity': quantity,
            'total': round(item.price * quantity, 2)
        })
    return items_in_receipt
