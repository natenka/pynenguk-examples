from pprint import pprint

lines = [
    "R1#show ip interface brief\n",
    "\n",
    "Interface           IP-Address    OK? Method Status   Protocol\n",
    "FastEthernet0/0     15.0.15.1     YES manual up       up\n",
    "FastEthernet0/1     10.0.12.1     YES manual up       up\n",
    "FastEthernet0/2     10.0.13.1     YES manual down     down\n",
    "FastEthernet0/3     unassigned    YES unset  up       down\n",
]
for line in lines:
    columns = line.split()
    # print(columns)
    if len(columns) > 5 and (columns[-1] == "up" or columns[-1] == "down"):
        print(columns)
