
ip_list = ["10.1.1.1", "10.1.10.1", "10.1.2.1", "10.1.11.1"]


def ip_to_bin(ip):
    octets = ip.split(".")
    octets_bin = []
    for octet in octets:
        oct_bin = f"{int(octet):08b}"
        octets_bin.append(oct_bin)
    return "".join(octets_bin)


print(sorted(ip_list, key=ip_to_bin))
