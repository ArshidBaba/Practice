class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        # print(f"An instance created: {name}")
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 2)
item2 = Item("Laptop", 1000, 3)
item1.apply_discount()

item2.pay_rate = 0.7
print(item1.price)

# item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# print(Item.__dict__)
# print(item1.__dict__)
