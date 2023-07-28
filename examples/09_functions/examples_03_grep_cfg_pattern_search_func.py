from pprint import pprint


def any_pattern_in_line(line, pattern_list):
    for pattern in pattern_list:
        if pattern in line:
            return True
    return False


def grep_cfg(filename, pattern_list):
    if type(pattern_list) == str:
        pattern_list = [pattern_list]
    lines = []
    with open(filename) as f:
        for line in f:
            if any_pattern_in_line(line, pattern_list):
                lines.append(line)
    return lines


result = grep_cfg("configs/config_r1.txt", ("interface", "ip address"))
pprint(result)
pprint(grep_cfg("configs/config_r1.txt", "alias"))


