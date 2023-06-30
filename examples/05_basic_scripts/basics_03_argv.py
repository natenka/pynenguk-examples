import sys

print(sys.argv)

# from sys import argv
# print(argv)

access_str = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

print(access_str.format(42))
