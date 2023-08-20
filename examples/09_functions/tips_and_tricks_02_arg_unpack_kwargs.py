def config_interface(intf, ip, mask):
    commands = [
        f"interface {intf}", "no shutdown", f"ip address {ip} {mask}"
    ]
    return commands

# intf1 = {"intf": "Gi0/1", "ip": "10.0.1.1", "mask": "255.255.255.0"}
# print(config_interface(intf="Gi0/1", ip="10.0.1.1", mask="255.255.255.0"))
# print(config_interface(**intf1))


interfaces_info = [
    {"intf": "Gi0/1", "ip": "10.0.1.1", "mask": "255.255.255.0"},
    {"intf": "Gi0/2", "ip": "10.0.2.1", "mask": "255.255.255.0"},
    {"intf": "Gi0/3", "ip": "10.0.3.1", "mask": "255.255.255.0"},
    {"intf": "Gi0/4", "ip": "10.0.4.1", "mask": "255.255.255.0"},
]

for info in interfaces_info:
    print(config_interface(**info))
