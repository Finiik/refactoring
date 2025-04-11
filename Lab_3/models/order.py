from models.order_item import OrderItem

class Order:
    def __init__(self, order_id, user):
        self.id = order_id
        self.user = user
        self.items = []

    def add_product(self, product, quantity):
        self.items.append(OrderItem(product, quantity))

    def remove_product(self, product):
        self.items = [item for item in self.items if item.product.id != product.id]

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)