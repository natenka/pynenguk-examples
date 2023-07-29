from pprint import pprint
"""
{'Ethernet0/0': '10.0.13.1',
 'Ethernet0/2': '10.0.19.1',
 'Loopback0': '10.1.1.1'}
"""

cfg = "configs/cfg.txt"

intf_ip_dict = {}
with open(cfg) as f:
	for line in f:
		if line.startswith("interface"):
			intf = line.split()[-1]
			# print(f"{intf=}")
			intf_ip_dict[intf] = None
		elif line.startswith(" ip address"):
			ip = line.split()[2]
			# print(f"{intf=} {ip=}")
			intf_ip_dict[intf] = ip

pprint(intf_ip_dict)
