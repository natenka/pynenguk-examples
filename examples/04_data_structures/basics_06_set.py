
# empty set
vlans = set()
print(vlans)

# literal
vlans = {1, 2, 10, 20}
print(vlans)

# set from list
vlans = [1, 10, 11, 20, 100]
vlans_set = set(vlans)
print(vlans_set)

# set from str
line = "test line"
letters = set(line)
print(letters)

# hashable items
items = {1, "test", (1, 2, 3)}

# всередині кортежу, який знаходиться в множині, повинні бути хешовані типи даних
# так можна
items = {1, "test", (1, 2, 3)}
# а ось так ні
# items = {1, "test", (1, [1, 2])}
