# from rich.traceback import install
# install()
# install(show_locals=True, extra_lines=5)


vlans = ["1", "2", "3", "test", "4", "5",
         "100", "2000", "switchport mode trunk"]


vlans_list = []
for vl in vlans:
    # if vl.isdigit():
    new_vl = int(vl)
    vlans_list.append(new_vl)

print(vlans_list)
