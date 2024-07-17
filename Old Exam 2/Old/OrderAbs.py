from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from PaymentType import PaymentType
from Order import Order
from OrderType import OrderType
from Customer import Customer
from CustomerType import CustomerType


class OrderAbs(Order, CustomerType, ABC):
    def __int__(self, order_id: int, order_name: str, delivery_address: str, list_of_items_in_the_order: list, order_customer, order_total_price: float, payment_type: PaymentType, order_date: datetime, order_type: OrderType):
        Order.__init__(order_id, order_name, delivery_address, list_of_items_in_the_order, order_customer, order_total_price, payment_type, order_date, order_type)

    @abstractmethod
    # Checking for Unique OrderId, Id must be unique
    def check_order_id(self):
        pass

    @abstractmethod
    # Calculates the total price of the order
    def calculate_order_total_price(self):
        item_price = 0
        order_total_price = 0
        if Order.order_type != 'VIP Order':
            order_total_price = sum(float(item_price) for item in Order.list_of_items_in_the_order) * Customer.customer_type
            return order_total_price
        else:
            order_total_price = sum(float(item_price) for item in Order.list_of_items_in_the_order)
            return order_total_price