from pprint import pprint

access_str = """
switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

intf = input("Введіть номер інтерфейсу: ")
vlan = input("Введіть номер влану: ")
# pprint(vlan)
print("interface {}".format(intf))
print(access_str.strip().format(vlan))

