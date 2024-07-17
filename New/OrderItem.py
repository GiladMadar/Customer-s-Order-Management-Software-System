class OrderItem:
    def __init__(self, item_id: int, item_name: str, item_price: float):
        # Constructor
        # Checking the type of the Args
        assert isinstance(item_id, int), "Item ID must be an integer."
        assert isinstance(item_name, str), "Item name must be a string."
        assert isinstance(item_price, float), "Item price must be a float."

        self.id = item_id
        self.name = item_name
        self.price = item_price

    #   Printing OrderItem Info - Magic Method
    def __repr__(self):
        return f"OrderItem(id={self.id}, name={self.name}, price={self.price})"
