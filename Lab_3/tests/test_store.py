import pytest
from models.user import User
from models.product import Product
from models.order import Order

@pytest.fixture
def setup_store():
    user = User(1, "TestUser", "test@example.com")
    product1 = Product(1, "Book", 15.0)
    product2 = Product(2, "Pen", 1.5)
    return user, product1, product2

def test_user_registration(setup_store):
    user, _, _ = setup_store
    assert user.register() == "User TestUser registered."

def test_user_login(setup_store):
    user, _, _ = setup_store
    assert user.login() == "User TestUser logged in."

def test_add_product_to_order(setup_store):
    user, product, _ = setup_store
    order = Order(1, user)
    order.add_product(product, 2)
    assert len(order.items) == 1
    assert order.items[0].quantity == 2

def test_remove_product_from_order(setup_store):
    user, product, _ = setup_store
    order = Order(1, user)
    order.add_product(product, 2)
    order.remove_product(product)
    assert len(order.items) == 0

def test_calculate_total(setup_store):
    user, p1, p2 = setup_store
    order = Order(1, user)
    order.add_product(p1, 1)
    order.add_product(p2, 2)
    assert order.calculate_total() == 18.0

def test_user_view_orders(setup_store):
    user, p1, _ = setup_store
    order = Order(1, user)
    order.add_product(p1, 1)
    user.orders.append(order)
    assert user.view_orders()[0] == order

def test_order_item_total_price(setup_store):
    _, p1, _ = setup_store
    from models.order_item import OrderItem
    item = OrderItem(p1, 3)
    assert item.get_total_price() == 45.0

def test_multiple_orders(setup_store):
    user, p1, _ = setup_store
    for i in range(3):
        order = Order(i, user)
        order.add_product(p1, 1)
        user.orders.append(order)
    assert len(user.view_orders()) == 3

def test_order_with_no_items_total(setup_store):
    user, _, _ = setup_store
    order = Order(1, user)
    assert order.calculate_total() == 0

def test_add_and_remove_products(setup_store):
    user, p1, p2 = setup_store
    order = Order(1, user)
    order.add_product(p1, 2)
    order.add_product(p2, 3)
    order.remove_product(p1)
    assert len(order.items) == 1
    assert order.items[0].product == p2
    
def test_user_creates_order_and_adds_products(setup_store):
    user, p1, p2 = setup_store
    order = Order(1, user)
    order.add_product(p1, 2)
    order.add_product(p2, 3)
    user.orders.append(order)

    assert len(user.orders) == 1
    assert user.orders[0].calculate_total() == (2 * p1.price + 3 * p2.price)

def test_user_multiple_orders_with_different_products(setup_store):
    user, p1, p2 = setup_store

    order1 = Order(1, user)
    order1.add_product(p1, 1)

    order2 = Order(2, user)
    order2.add_product(p2, 4)

    user.orders.append(order1)
    user.orders.append(order2)

    assert len(user.orders) == 2
    assert user.orders[0].calculate_total() == p1.price
    assert user.orders[1].calculate_total() == 4 * p2.price

def test_order_item_links_product_correctly(setup_store):
    _, p1, _ = setup_store
    from models.order_item import OrderItem
    item = OrderItem(p1, 2)

    assert item.product.name == "Book"
    assert item.get_total_price() == 2 * p1.price

def test_order_contains_correct_order_items(setup_store):
    user, p1, p2 = setup_store
    order = Order(1, user)
    order.add_product(p1, 1)
    order.add_product(p2, 2)

    assert order.items[0].product == p1
    assert order.items[1].product == p2
    assert order.items[1].quantity == 2

def test_user_order_workflow_end_to_end(setup_store):
    user, p1, p2 = setup_store
    assert user.login() == "User TestUser logged in."

    order = Order(10, user)
    order.add_product(p1, 2)
    order.add_product(p2, 5)
    user.orders.append(order)
    expected_total = (2 * p1.price + 5 * p2.price)
    assert order.calculate_total() == expected_total
    orders = user.view_orders()
    assert len(orders) == 1
    assert orders[0].id == 10
