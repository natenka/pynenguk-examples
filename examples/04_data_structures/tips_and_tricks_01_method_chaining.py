cmd = "switchport trunk allowed vlan 10,20,30"

words = cmd.split()
vlans_str = words[-1]
vlans = vlans_str.split(",")
print(vlans)
