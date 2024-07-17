from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from PaymentType import PaymentType
from Order import Order
from OrderType import OrderType
from Customer import Customer
from CustomerType import CustomerType

class Orders(Order, Customer, ABC):
    def __int__(self, order_id: int, order_name: str, delivery_address: str, list_of_items_in_the_order: list, order_customer: Customer, order_total_price: float, payment_type: PaymentType, order_date: datetime, customer_id, first_name: str, last_name: str, email: str, delivery_address: str, customer_type: CustomerType, customer_discount: float, favorite_items: list, customer_gift: str):
        Order.__init__(order_id, order_name, delivery_address, list_of_items_in_the_order, order_customer, order_total_price, payment_type, order_date)
        Customer.__init__(customer_id, first_name, last_name, email, delivery_address, customer_type, customer_discount, favorite_items, customer_gift)