import sys

print(sys.argv)

# from sys import argv
# print(argv)

if len(sys.argv) == 3:
    intf = sys.argv[1]
    vlan = sys.argv[2]
else:
    intf = "Gi0/0"
    vlan = 1

access_str = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

print("interface {}".format(intf))
print(access_str.format(vlan))
