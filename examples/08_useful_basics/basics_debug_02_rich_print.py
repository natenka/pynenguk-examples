# from rich import print as rprint
from rich import print, inspect
from pprint import pprint


vlans = ["1", "2", "3", "4", "5", "line1\nline2\n", "test", "switchport access vlan 10"]
# inspect(vlans, methods=True)
print(vlans)

vlans_list = []
for vl in vlans:
    if vl.isdigit():
        new_vl = int(vl)
        vlans_list.append(new_vl)
        print(f"{vl=} {new_vl=} {vlans_list=}")

print(vlans_list)
