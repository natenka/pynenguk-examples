sw1 = {1, 2, 3, 10, 20}
sw2 = {30, 40, 100, 10, 20}
sw3 = [10, 100, 200, 300]


# перетин
common_vlans = sw1.intersection(sw2)
common_vlans = sw1 & sw2
print(common_vlans)

common_vlans = sw1.intersection(sw2, sw3)
common_vlans = sw1 & sw2 & set(sw3)
print(common_vlans)


# об'єднання
all_vlans = sw1.union(sw2)
all_vlans = sw1 | sw2

all_vlans = sw1.union(sw2, sw3)
all_vlans = sw1 | sw2 | set(sw3)


# різниця
diff12 = sw1.difference(sw2)
diff12 = sw1 - sw2
diff21 = sw2.difference(sw1)
diff21 = sw2 - sw1

sym_diff = sw1.symmetric_difference(sw2)
sym_diff = sw1 ^ sw2
