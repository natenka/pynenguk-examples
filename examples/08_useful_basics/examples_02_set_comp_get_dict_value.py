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
        "ios": "15.5",
        "ip": "10.255.0.3",
    },
    "sw1": {
        "hostname": "london_sw1",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
    },
}

ios_set = {dev["ios"] for dev in devices.values()}
ios_set = {dev["ios"] for dev in devices.values() if "ios" in dev}

# ios_set = set()
#
# for dev in devices.values():
#     ios_set.add(dev["ios"])
