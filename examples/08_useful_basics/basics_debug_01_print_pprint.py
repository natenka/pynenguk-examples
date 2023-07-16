vlans = ["1", "2", "3", "test", "4", "5", "switchport allowed vlans add", "100", "2000", "switchport mode trunk"]
from pprint import pprint
vlans = ["1", "2", "3", "4", "5", "line1\nline2\n", "test"]


pprint(vlans)
vlans_list = []
for vl in vlans:
    if vl.isdigit():
        new_vl = int(vl)
        vlans_list.append(new_vl)
        print(f"{vl=} {new_vl=} {vlans_list=}")

print(vlans_list)
