import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all_items = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validation for received arguments
        assert price >= 0, f"Your Price={price} can't be equal or less than zero"
        assert quantity >= 0, f"Your quantity={quantity} can't be equal or less than zero"

        self.__name = name
        self.price = price
        self.quantity = quantity

        # add all items to all_items list
        Item.all_items.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as items_file:
            reader = csv.DictReader(items_file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
