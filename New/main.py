from Order import Order
from OrderItem import OrderItem
from Gift import Gift
from Customer import Customer

if __name__ == '__main__':
    # Create some items
    item1 = OrderItem(item_id=1, item_name="Item1", item_price=100)
    item2 = OrderItem(item_id=2, item_name="Item2", item_price=200)

    # Create a regular customer
    customer1 = Customer(customer_id=1, first_name="John", last_name="Doe", email="john@example.com", delivery_address="123 Street", customer_type="REGULAR")

    # Create a VIP customer
    customer2 = Customer(customer_id=2, first_name="Jane", last_name="Doe", email="jane@example.com", delivery_address="456 Avenue", customer_type="VIP", customer_discount=0.10)

    # Create a regular order
    order1 = Order(order_id=1, name="Order1", delivery_address="123 Street", items=[item1, item2], customer=customer1, payment_type="CREDIT CARD", order_date="2024-07-17")

    # Create a VIP order
    order2 = Order(order_id=2, name="Order2", delivery_address="456 Avenue", items=[item1], customer=customer2, payment_type="CREDIT CARD", order_date="2024-07-17", is_vip=True)

    # Print the orders to verify their creation
    print(order1)
    print(order2)

    # Add items to customer's favorite list and print the list
    customer1.add_favorite_item(item1)
    customer1.add_favorite_item(item2)
    print(customer1.favorite_items)

    # Gift operations
    gift = Gift()
    customer1.take_gift(gift)
    customer1.open_gift()
