value = input("Що вивести? [ip/mac/mask]: ")

if value == "ip":
    print("10.1.1.1")
elif value == "mac":
    print("aaaa:bbbb:cccc")
elif value == "mask":
    print("24")
elif value == "hostname":
    print("sw1")
else:
    print("Такого параметру немає")

choice = {
    "ip": "10.1.1.1",
    "mac": "aaaa:bbbb:cccc",
    "mask": "24",
    "hostname": "sw1",
}
# print(choice[value])
print(choice.get(value, "Такого параметру немає"))
