from ...modules.models import Item

class Database:
    def __init__(self, items=[]):
        self.items = items
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_item_by_id(self, id):
        for item in self.items:
            if item.id == id:
                return item
        raise Exception(f'There is no such item with id={id}.')


def test_db_setup():
    return Database(
        [
            Item(id=1, title='Вода', price=69.90),
            Item(id=2, title='Чай', price=119),
            Item(id=3, title='Кофе', price=169.99),
            Item(id=4, title='Молоко', price=85.2),
        ]
    )
