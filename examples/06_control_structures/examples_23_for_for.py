commands = [
    "switchport mode access",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
intf_list = ["0/1", "0/3", "0/4", "0/11"]


for intf in intf_list:
    print(f"interface Gi{intf}")
    for cmd in commands:
        print(cmd)

"""
interface Gi0/1
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
interface Gi0/3
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
interface Gi0/4
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
"""

