# В задании не предлагается сохранение данных в БД, поэтому избежим использования ORM.

class Item:
    def __init__(self, id: int, title: str, price: float):
        self.id = id
        self.title = title
        self.price = price

    def __repr__(self):
        return f"<Item(id={self.id}, title='{self.title}', price={self.price})>"
