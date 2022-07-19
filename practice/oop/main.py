from item import Item

from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("logitech", 750, 6)

item2 = Phone("iPhone12", 1000, 3)

item1.apply_discount()

print(item1.price)

item2.apply_discount()

print(item2.price)
