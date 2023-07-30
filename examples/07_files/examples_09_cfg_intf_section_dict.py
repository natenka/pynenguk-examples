from pprint import pprint

{
    "Ethernet0/0": [
        "description To PE_r3 Ethernet0/0",
        "bandwidth 100000",
        "ip address 10.0.13.1 255.255.255.0",
        "mpls traffic-eng tunnels",
        "ip rsvp bandwidth 100000 10000",
    ],
    "Ethernet0/1": ["no ip address"],
    "Ethernet0/2": [
        "description To P_r9 Ethernet0/2",
        "ip address 10.0.19.1 255.255.255.0",
        "mpls traffic-eng tunnels",
        "ip rsvp bandwidth",
    ],
}
src_file = "configs/config_r1.txt"

intf_section_dict = {}
with open(src_file) as src:
    intf_section = False
    for line in src:
        if line.startswith("interface"):
            intf = line.split()[-1]
            intf_section = True
            intf_cmd_list = []
            intf_section_dict[intf] = intf_cmd_list
        elif line.startswith(" "):
            if intf_section:
                intf_cmd_list.append(line.strip())

        else:
            intf_section = False
pprint(intf_section_dict)

#intf_section_dict = {}
#with open(src_file) as src:
#    intf_section = False
#    for line in src:
#        if line.startswith("interface"):
#            intf = line.split()[-1]
#            intf_section = True
#            intf_section_dict[intf] = []
#        elif line.startswith(" "):
#            if intf_section:
#                intf_section_dict[intf].append(line)
#        else:
#            intf_section = False
