
vlan_list = ["1", "2", "trunk", "3", "4", "mode", " 5"]

vlans_int = []
for vl in vlan_list:
    vl = vl.strip()
    if vl.isdigit():
        vlans_int.append(int(vl))

print(vlans_int)
