

def config_interface(intf_name, ip_address, mask):
    interface = f"interface {intf_name}"
    no_shut = "no shutdown"
    ip_addr = f"ip address {ip_address} {mask}"
    result = [interface, no_shut, ip_addr]
    return result


# print(config_interface("Fa0/1", "10.0.1.1", "255.255.255.0"))
interfaces_info = [
    ["Fa0/1", "10.0.1.1", "255.255.255.0"],
    ["Fa0/2", "10.0.2.1", "255.255.255.0"],
    ["Fa0/3", "10.0.3.1", "255.255.255.0"],
    ["Fa0/4", "10.0.4.1", "255.255.255.0"],
]

for info in interfaces_info:
    print(config_interface(*info))
    print(config_interface(info[0], info[1], info[2]))

