from pprint import pprint


def read_cfg_to_list(filename):
    result = []
    with open(filename) as f:
        for line in f:
            if not line.startswith("!"):
                result.append(line.strip())

    return result


cfg1 = "configs/cfg1.txt"
lines = read_cfg_to_list(cfg1)
print(lines)

cfg2 = "configs/cfg2.txt"
lines = read_cfg_to_list(cfg2)
print(lines)
