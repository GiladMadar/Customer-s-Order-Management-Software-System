from datetime import datetime, timedelta
from PaymentType import PaymentType
from OrderType import OrderType
from Customer import Customer

class Order:
    #   Order Constructor
    def __init__(self, order_id: int, order_name: str, delivery_address: str, list_of_items_in_the_order: list, order_customer: Customer, order_total_price: float, payment_type: PaymentType, order_date: datetime):
        #   assert

        self.id = order_id
        self.order_name = order_name
        self.delivery_address = delivery_address
        self.list_of_items_in_the_order = list_of_items_in_the_order
        self.order_customer = order_customer
        self.order_total_price = order_total_price
        self.payment_type = payment_type
        self.order_date = order_date
        self.order_type = OrderType.check_order_type()




