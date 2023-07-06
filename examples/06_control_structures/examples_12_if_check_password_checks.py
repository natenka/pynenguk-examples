password = "123test456"

# counter
counter = 0
for sym in password:
    if sym.isdigit():
        counter += 1
print(counter)

# set
password = "123test123"
count_int = set()

for sym in password:
    if sym.isdigit():
        count_int.add(sym)
print(count_int)

# set intersection
password = "123test123"
print(set(password) & set("0123456789"))

