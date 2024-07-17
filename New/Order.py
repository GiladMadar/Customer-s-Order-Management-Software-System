import Customer


class Order(Customer):
    def __init__(self, order_id, name, delivery_address, items, customer: Customer, payment_type, order_date, is_vip=False):
        assert isinstance(order_id, int), "Order ID must be an integer."
        assert isinstance(name, str), "Order name must be a string."
        assert isinstance(delivery_address, str), "Delivery address must be a string."
        assert isinstance(items, list), "Items must be a list of OrderItem objects."
        assert isinstance(customer, object), "Customer must be a Customer object."
        assert isinstance(payment_type, str), "Payment type must be a string."
        assert isinstance(order_date, str), "Order date must be a string in the format YYYY-MM-DD."
        assert isinstance(is_vip, bool), "is_vip must be a boolean."
        assert payment_type in ["CREDIT CARD", "DEBIT CARD"], "Invalid payment type."
        assert is_vip in [True, False], "is_vip must be a boolean."

        self.id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date
        self.is_vip = is_vip
        self.total_price = self.calculate_total_price()
        self.validate_order()

    def calculate_total_price(self):
        total = sum(item.price for item in self.items)
        if self.is_vip:
            if self.super().customer_type == "VIP" and self.super().customer_discount:
                total *= (1 - self.super().customer_discount)
            else:
                raise ValueError("Order marked as VIP but customer is not VIP or discount is missing.")
        return total

    def validate_order(self):
        if self.is_vip and self.super().customer_type != "VIP":
            raise ValueError("VIP order can only be placed by VIP customers.")

    def __repr__(self):
        return f"Order(id={self.id}, name={self.name}, total_price={self.total_price})"
