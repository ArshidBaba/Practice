from item import Item


class Phone(Item):
    # all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than zero!"

        self.broken_phones = broken_phones

        # Phone.all.append(self)
