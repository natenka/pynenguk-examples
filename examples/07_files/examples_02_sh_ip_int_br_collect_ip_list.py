from pprint import pprint

filename = "show_output/sh_ip_int_br.txt"
ip_list = []
with open(filename) as f:
    for line in f:
        columns = line.split()
        if len(columns) > 5 and columns[1][0].isdigit():
            ip_list.append(columns[1])

print(ip_list)
