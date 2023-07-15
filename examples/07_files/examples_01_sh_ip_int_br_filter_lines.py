from pprint import pprint

filename = "show_output/sh_ip_int_br.txt"
with open(filename) as f:
    for line in f:
        # pprint(line)
        columns = line.split()
        if len(columns) > 5 and columns[1][0].isdigit():
            print(columns)


#        if "up" in line:
#        if "up" in line or "down" in line:
#        if line.count("up") == 2:
#        if len(columns) > 5 and columns[-1] == "up":
#        if len(columns) > 5 and (columns[-1] == "up" or columns[-1] == "down"):
#        if len(columns) > 5 and columns[-1] in ["up", "down"]:
#        if len(columns) > 5 and columns[1] != "unassigned":
#        if len(columns) > 5 and columns[1][0].isdigit():


with open(filename) as f:
    for line in f:
        # pprint(line)
        columns = line.split()
        try:
            ip = columns[1]
        except IndexError:
            pass
        else:
            if ip[0].isdigit():
                print(columns)
