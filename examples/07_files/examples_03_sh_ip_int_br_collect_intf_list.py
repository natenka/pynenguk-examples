"""
[['FastEthernet0/0', '15.0.15.1', 'up'],
 ['FastEthernet0/1', '10.0.12.1', 'up'],
 ['FastEthernet0/2', '10.0.13.1', 'down'],
 ['FastEthernet0/3', 'unassigned', 'down'],
 ['Loopback0', '10.1.1.1', 'up'],
 ['Loopback100', '100.0.0.1', 'up']]
"""
from pprint import pprint

filename = "show_output/sh_ip_int_br.txt"
intf_info = []
with open(filename) as f:
    for line in f:
        columns = line.split()
        if len(columns) > 5 and columns[-1] in ("up", "down"):
            # print(columns)
            intf = columns[0]
            ip = columns[1]
            status = columns[-1]
            intf_info.append([intf, ip, status])
pprint(intf_info)

