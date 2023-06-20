device_template = "Hostname: {host} IP: {ip} Model: {model}"

print(device_template.format(model="C3850", host="sw1", ip="10.1.1.1"))


template1 = "Hostname: {host} IP: {ip} Model: {model} URL: https://api.../{ip}/{host}/{model}"
print(template1.format(model="C3850", host="sw1", ip="10.1.1.1"))

template2 = "Hostname: {0} IP: {1} Model: {2} URL: https://api.../{1}/{0}/{2}"
print(template2.format("sw1", "10.1.1.1", "C3850"))

