from pprint import pprint


def grep_cfg(filename, patterns):
    lines = []
    # if isinstance(patterns, str):
    if type(patterns) == str:
        patterns = [patterns]
    with open(filename) as f:
        for line in f:
            for pattern in patterns:
                if pattern in line:
                    lines.append(line)
                    break
    return lines



pprint(grep_cfg("configs/config_r1.txt", "ip address"))
result = grep_cfg("configs/config_r1.txt", ("interface", "address"))
pprint(result)
