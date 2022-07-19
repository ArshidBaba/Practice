from re import I
from item import Item

# from phone import Phone

item1 = Item("MyItem", 750)
item1.name = "OtherItem"

# print(item1.read_only_name)

# item1.read_only_name = "BBB"
# item1.price = 900
item1.apply_increment(0.2)
print(item1.price)
