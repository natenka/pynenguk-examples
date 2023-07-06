vlan_list = ["1", "2", "trunk", "3", "4", "mode", "5"]

vlans_int = []
for vl in vlan_list:
    if vl.isdigit():
        new_vl = int(vl)
        vlans_int.append(new_vl)

print(vlans_int)
