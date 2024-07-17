from abc import ABC, abstractmethod

from CustomerType import CustomerType


class Customer(ABC):
    def __int__(self, customer_id, first_name: str, last_name: str, email: str, delivery_address: str, customer_type: CustomerType, customer_discount: float, favorite_items: list, customer_gift: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = favorite_items
        self.customer_gift = customer_gift



