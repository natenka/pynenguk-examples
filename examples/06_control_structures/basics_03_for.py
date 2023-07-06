cmd = "switchport trunk allowed vlan 10,20,30,40,50"
vlans_list = cmd.split()[-1].split(",")
# vlans_list = ['10', '20', '30', '40', '50']
print(vlans_list)

vlans = []
for vl in vlans_list:
    vl_int = int(vl)
    vlans.append(vl_int)

print(vlans)

