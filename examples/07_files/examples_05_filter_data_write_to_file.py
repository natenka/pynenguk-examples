from pprint import pprint

src_file = "show_output/sh_ip_int_br.txt"
dst_file = "result_lines.txt"

result = []
with open(src_file) as src:
    for line in src:
        if line.count("up") == 2:
            result.append(line)
# pprint(result)

with open(dst_file, "w") as dst:
    for line in result:
        dst.write(line)


# записуємо одразу
with open(src_file) as src, open(dst_file, "w") as dst:
    for line in src:
        if line.count("up") == 2:
            dst.write(line)

