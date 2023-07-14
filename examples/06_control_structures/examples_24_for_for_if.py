access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access = {"0/12": 10, "0/14": 11, "0/16": 17, "0/17": 150}
for intf, vlan in access.items():
	print(f"interface Gi{intf}")
	for cmd in access_template:
		if cmd.endswith("vlan"):
			cmd = f"{cmd} {vlan}"
		print(f" {cmd}")


"""
interface Gi0/12
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
interface Gi0/14
 switchport mode access
 switchport access vlan 11
 spanning-tree portfast
 spanning-tree bpduguard enable
interface Gi0/16
 switchport mode access
 switchport access vlan 17
 spanning-tree portfast
 spanning-tree bpduguard enable
interface Gi0/17
 switchport mode access
 switchport access vlan 150
 spanning-tree portfast
 spanning-tree bpduguard enable
"""
