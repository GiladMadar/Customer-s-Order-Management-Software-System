from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from Order import Order
from PaymentType import PaymentType


class OrderType(ABC, Order):
    def __init__(self, order_id: int, order_name: str, delivery_address: str, list_of_items_in_the_order: list, order_customer, order_total_price: float, payment_type: PaymentType, order_date: datetime):
        super().__init__(order_id, order_name, delivery_address, list_of_items_in_the_order, order_customer, order_total_price, payment_type, order_date)

    def regular_order(self):
        pass

    def vip_order(self):
        pass

    def check_order_type(self):
        pass