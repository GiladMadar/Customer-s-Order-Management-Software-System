from Order import Order
from OrderItem import OrderItem
from Customer import Customer
from Gift import ConcreteGift

if __name__ == '__main__':
    print("\n\n-------------------------------------------------------- Start --------------------------------------------------------\n\n")
    # Testing the OrderItem class
    print("                                        Customer’s Order Management Software System:\n\n")
    print("Testing OrderItem class:\n")

    # Create some items
    item1 = OrderItem(item_id=1, item_name="Item1", item_price=100.00)
    item2 = OrderItem(item_id=2, item_name="Item2", item_price=200.00)

    # Printing the Items
    print(f" - Item 1: {item1}\n")
    print(f" - Item 2: {item2}\n")

    # Testing the Customer class
    print("Testing Customer class:\n")

    # Create a regular customer
    customer1 = Customer(customer_id=1, first_name="John", last_name="Doe", email="john@example.com",
                         delivery_address="123 Street", customer_type="REGULAR")
    # Printing Customer1 info
    print(f" - Customer 1: {customer1}")

    # Create a VIP customer
    customer2 = Customer(customer_id=2, first_name="Jane", last_name="Doe", email="jane@example.com",
                         delivery_address="456 Avenue", customer_type="VIP", customer_discount=0.10)
    # Printing Customer2 info
    print(f" - Customer 2: {customer2}\n")

    # Testing the Order class
    print("Testing Order class:\n")

    # Create a regular order
    order1 = Order(order_id=1, name="Order1", delivery_address="123 Street", items=[item1, item2], customer=customer1,
                   payment_type="CREDIT CARD", order_date="2024-07-17")

    # Create a VIP order
    order2 = Order(order_id=2, name="Order2", delivery_address="456 Avenue", items=[item1], customer=customer2,
                   payment_type="CREDIT CARD", order_date="2024-07-17", is_vip=True)

    # Print the orders to verify their creation
    print(f" - Order 1: {order1}")
    print(f" - Order 2: {order2}\n")

    # Testing favorite items functionality
    print("Testing Customer's favorite items functionality:\n")

    # Add items to customer's favorite list and print the list
    customer1.add_favorite_item(item1)
    customer1.add_favorite_item(item2)
    print(f" - Customer 1's favorite items: {customer1.favorite_items}\n")

    # Testing Gift operations
    print("Testing Gift operations:\n")

    gift = ConcreteGift()
    customer1.take_gift(gift)
    customer1.open_gift()
    print("\n\n-------------------------------------------------------- End --------------------------------------------------------")
