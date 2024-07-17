from New.Gift import Gift


class Customer(Gift):
    def __init__(self, customer_id, first_name, last_name, email, delivery_address, customer_type, customer_discount=None):
        assert isinstance(customer_id, int), "Customer ID must be an integer."
        assert isinstance(first_name, str), "First name must be a string."
        assert isinstance(last_name, str), "Last name must be a string."
        assert isinstance(email, str), "Email must be a string."
        assert isinstance(delivery_address, str), "Delivery address must be a string."
        assert customer_type in ["REGULAR", "VIP"], "Invalid customer type."
        # Customer discount Should be in percentage 0.[Percentage] or None
        assert customer_discount is None or (0 <= customer_discount <= 1), "Customer discount must be between 0 and 1."

        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = []
        self.gift = None

    def add_favorite_item(self, item):
        if item.name not in [i.name for i in self.favorite_items]:
            self.favorite_items.append(item)

    def remove_favorite_item(self, item_name):
        self.favorite_items = [item for item in self.favorite_items if item.name != item_name]

    def take_gift(self, gift):
        self.gift = gift

    def open_gift(self):
        if self.gift:
            print("Congratulations! you got a new gift! Enjoy!")
        else:
            print("No gift to open.")

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.first_name} {self.last_name}, type={self.customer_type})"
