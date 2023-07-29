from pprint import pprint


def any_pattern_in_line(line, patterns):
    if type(patterns) == str:
        patterns = [patterns]
    for pattern in patterns:
        if pattern in line:
            return True
    return False


def grep_cfg(filename, patterns):
    lines = []
    with open(filename) as f:
        for line in f:
            if any_pattern_in_line(line, patterns):
                lines.append(line)
    return lines



pprint(grep_cfg("configs/config_r1.txt", "ip address"))
result = grep_cfg("configs/config_r1.txt", ("interface", "address"))
pprint(result)
