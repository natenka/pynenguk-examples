from pprint import pprint

"""
{'r1': {'Ethernet0/0': '10.0.13.1',
        'Ethernet0/2': '10.0.19.1',
        'Loopback0': '10.1.1.1'},
 'r2': {'Ethernet0/0': '10.0.23.2',
        'Ethernet0/1': '10.255.2.2',
        'Ethernet0/2': '10.0.29.2',
        'Loopback0': '10.2.2.2'},
 'r3': {'Ethernet0/0': '10.0.13.3', 'Loopback0': '10.3.3.3'},
 'sw1': {'Vlan100': '10.0.100.1'}}
"""

def get_intf_ip_dict_from_cfg(filename):
    intf_ip_dict = {}

    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
                # intf_ip_dict[intf] = None
            elif line.startswith(" ip address"):
                ip = line.split()[2]
                intf_ip_dict[intf] = ip
    return intf_ip_dict


def get_host_intf_ip_dict(config_list):
    host_intf_dict = {}
    for cfg in config_list:
        hostname = cfg.split("_")[-1].split(".")[0]
        intf_ip_dict = get_intf_ip_dict_from_cfg(cfg)
        host_intf_dict[hostname] = intf_ip_dict
    return host_intf_dict

path = "/home/vagrant/repos/uk/examples/examples/09_functions/"
cfg_list = [
    "configs/config_r1.txt",
    "configs/config_r2.txt",
    "configs/config_r3.txt",
    "configs/config_sw1.txt",
]
full_path = [f"{path}{f}" for f in cfg_list]
pprint(full_path)

pprint(get_host_intf_ip_dict(cfg_list))
pprint(get_host_intf_ip_dict(full_path))
