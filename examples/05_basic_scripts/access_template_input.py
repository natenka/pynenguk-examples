from pprint import pprint

intf = input("Interface: ")
vlan = input("VLAN: ")

access_str = """
switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

print(f"interface {intf}")
print(access_str.format(vlan))
