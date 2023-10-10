from collections import OrderedDict

ordered_items_with_net_price = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(' ',1)
    if item in ordered_items_with_net_price:
        ordered_items_with_net_price[item] += int(price)
    else:
        ordered_items_with_net_price[item] = int(price)

items = [print(f"{item} {price}") for item, price in ordered_items_with_net_price.items()]
