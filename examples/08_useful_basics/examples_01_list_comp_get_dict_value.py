devices = {
    "r1": {
        "hostname": "london_r1",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "hostname": "london_r2",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "r3": {
        "hostname": "london_r3",
        "ios": "15.4",
        "ip": "10.255.0.3",
    },
    "sw1": {
        "hostname": "london_sw1",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
    },
}


ip_list = [devices[hostname]["ip"] for hostname in devices]

# ip_list = []
# for hostname in devices:
#     ip_list.append(devices[hostname]["ip"])

ip_list = [dev["ip"] for dev in devices.values()]
ip_list = [dev.get("ip") for dev in devices.values()]

# ip_list = []
# for dev in devices.values():
#     ip_list.append(dev["ip"])

ip_list = [dev["ip"] for dev in devices.values() if "ip" in dev]

# ip_list = []
# for dev in devices.values():
#     if "ip" in dev:
#         ip_list.append(dev["ip"])
