"""
FastEthernet0/2     10.0.13.1      down
FastEthernet0/3     unassigned     down
FastEthernet0/0     15.0.15.1      up
FastEthernet0/1     10.0.12.1      up
Loopback0           10.1.1.1       up
Loopback100         100.0.0.1      up
"""
from pprint import pprint

filename = "show_output/sh_ip_int_br.txt"
result = []
with open(filename) as f:
    for line in f:
        if "up" in line or "down" in line:
            columns = line.split()
            intf, ip, protocol = columns[0], columns[1], columns[-1]
            result.append([intf, ip, protocol])

sorted_result = sorted(result)
#pprint(sorted_result)

for intf, ip, status in sorted_result:
    intf, ip, status = item
    print(f"{intf:20}{ip:20}{status}")

# сортування за protocol
result = []
with open(filename) as f:
    for line in f:
        if "up" in line or "down" in line:
            columns = line.split()
            intf, ip, protocol = columns[0], columns[1], columns[-1]
            result.append([protocol, intf, ip])

sorted_result = sorted(result)
pprint(sorted_result)

for status, intf, ip in sorted_result:
    print(f"{intf:20}{ip:20}{status}")
