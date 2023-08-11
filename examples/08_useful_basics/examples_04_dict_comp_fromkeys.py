devices = ["sw1", "sw2", "sw3", "r1"]

dev_dict = {host: None for host in devices}
# {'sw1': None, 'sw2': None, 'sw3': None, 'r1': None}

# dev_dict = dict.fromkeys(devices)

count_vlans = {host: 0 for host in devices}
# {'sw1': 0, 'sw2': 0, 'sw3': 0, 'r1': 0}

count_vlans = dict.fromkeys(devices, 0)

# в значенні один і той самий список!
# dev_params = dict.fromkeys(devices, [])

dev_params = {host: [] for host in devices}
# {'sw1': [], 'sw2': [], 'sw3': [], 'r1': []}

dev_params["sw1"].append(100)
