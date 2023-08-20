

def config_interface(intf, ip, mask):
    commands = [
        f"interface {intf}", "no shutdown", f"ip address {ip} {mask}"
    ]
    return commands


# print(config_interface("Gi0/1", "10.0.1.1", "255.255.255.0"))
# ['interface Gi0/1', 'no shutdown', 'ip address 10.0.1.1 255.255.255.0']

interfaces_info = [
    ["Gi0/1", "10.0.1.1", "255.255.255.0"],
    ["Gi0/2", "10.0.2.1", "255.255.255.0"],
    ["Gi0/3", "10.0.3.1", "255.255.255.0"],
    ["Gi0/4", "10.0.4.1", "255.255.255.0"],
]
for info in interfaces_info:
    # print(config_interface(info[0], info[1], info[2]))
    print(config_interface(*info))
