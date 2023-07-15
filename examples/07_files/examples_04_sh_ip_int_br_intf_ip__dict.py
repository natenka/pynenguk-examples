"""
{'FastEthernet0/0': '15.0.15.1',
 'FastEthernet0/1': '10.0.12.1',
 'FastEthernet0/2': '10.0.13.1',
 'FastEthernet0/3': None,
 'Loopback0': '10.1.1.1',
 'Loopback100': '100.0.0.1'}
"""
from pprint import pprint

filename = "show_output/sh_ip_int_br.txt"
intf_ip_dict = {}
with open(filename) as f:
    for line in f:
        columns = line.split()
        if len(columns) > 5 and columns[-1] in ("up", "down"):
            intf = columns[0]
            ip = columns[1]
            # if ip == "unassigned":
            #     intf_ip_dict[intf] = None
            # else:
            #     intf_ip_dict[intf] = ip
            if ip == "unassigned":
                ip = None
            intf_ip_dict[intf] = ip

pprint(intf_ip_dict)

