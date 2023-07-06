numbers = [10, 20, 30, 40, 50]

for index in range(5):
    print(index, numbers[index])

for index in range(len(numbers)):
    print(index, numbers[index])



vlans = [10, 20, 30, 40, 255]
vlan_names = ["IT", "Marketing", "Sales", "Support", "Native"]

for index in range(len(vlans)):
    print("vlan", vlans[index])
    print(" name", vlan_names[index])
