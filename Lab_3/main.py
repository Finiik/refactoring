from models.user import User
from models.product import Product
from models.order import Order

if __name__ == "__main__":
    user = User(1, "Ivan", "ivan@example.com")
    print(user.register())

    product1 = Product(101, "Phone", 500.0)
    product2 = Product(102, "Laptop", 1200.0)

    order = Order(1, user)
    order.add_product(product1, 2)
    order.add_product(product2, 1)

    user.orders.append(order)
    print(f"Total order price: {order.calculate_total()}")