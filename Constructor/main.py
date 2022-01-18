class Item:
    def __init__(self, name: str, price: float, quantity=0):

        # Validation for received arguments
        assert price >= 0, f"Your Price={price} can't be equal or less than zero"
        assert quantity >= 0, f"Your quantity={quantity} can't be equal or less than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item_1 = Item("Pen", 100, 5)
item_2 = Item("Notebook", 100, 5)

print(item_1.calculate_total_price())
print(item_2.calculate_total_price())
