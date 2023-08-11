
keys = ["hostname", "ip", "ios", "vendor"]
values = ["sw1", "10.1.1.1", "15.4", "Cisco"]


sw1 = {keys[index]: values[index] for index in range(len(keys))}
# {'hostname': 'sw1', 'ip': '10.1.1.1', 'ios': '15.4', 'vendor': 'Cisco'}

sw1 = {}
for index in range(len(keys)):
    sw1[keys[index]] = values[index]


# варіант 2
# list(zip(keys, values))
# [('hostname', 'sw1'), ('ip', '10.1.1.1'), ('ios', '15.4'), ('vendor', 'Cisco')]
sw1 = {key: value for key, value in zip(keys, values)}

sw1 = {}
for key, value in zip(keys, values):
    sw1[key] = value
