from pprint import pprint

with open("configs/config_r1.txt") as f:
    output = f.read()

result = {}
sections = output.split("!")
for section in sections:
    section = section.strip()
    if section.startswith("interface"):
        for line in section.split("\n"):
            if line.startswith("interface"):
                intf = line.split()[-1]
                result[intf] = []
            else:
                result[intf].append(line.strip())
pprint(result)
