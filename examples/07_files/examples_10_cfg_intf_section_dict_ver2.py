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
    for line in src:
        if line.startswith(" "):
            if section.startswith("interface"):
                intf = section.split()[-1]
                if intf not in intf_section_dict:
                    intf_section_dict[intf] = []
                intf_section_dict[intf].append(line.strip())
        else:
            section = line

pprint(intf_section_dict)


# intf_section_dict = {}
# with open(src_file) as src:
#     for line in src:
#         if not line.startswith(" "):
#             section = line
#             if section.startswith("interface"):
#                 intf_section_dict[section] = []
#         elif line.startswith(" "):
#             if section.startswith("interface"):
#                 intf_section_dict[section].append(line)
#
# pprint(intf_section_dict)
