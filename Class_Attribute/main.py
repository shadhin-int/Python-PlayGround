class Item:

    pay_rate = 0.8  # This pay rate after 20% dicount
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Validation for received arguments
        assert price >= 0, f"Your Price={price} can't be equal or less than zero"
        assert quantity >= 0, f"Your quantity={quantity} can't be equal or less than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item_1 = Item("Phone", 100, 1)
item_2 = Item("Laptop", 1000, 3)
item_3 = Item("Cable", 10, 5)
item_4 = Item("Mouse", 50, 5)
item_5 = Item("Keyboard", 75, 5)

print(Item.all)
