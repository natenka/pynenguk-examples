from pprint import pprint




result = get_intf_ip_dict_from_cfg("configs/config_r1.txt")
pprint(result)

"""
{'Ethernet0/0': '10.0.13.1',
 'Ethernet0/1': None,
 'Ethernet0/2': '10.0.19.1',
 'Ethernet0/3': None,
 'Ethernet0/3.100': None,
 'Ethernet1/0': None,
 'Loopback0': '10.1.1.1',
 'Tunnel0': None}
"""
