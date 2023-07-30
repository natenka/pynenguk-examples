from pprint import pprint


def grep_lines_start(filename, pattern):
    lines = []
    with open(filename) as f:
        for line in f:
            if line.startswith(pattern):
                lines.append(line)
    return lines


def grep_lines_end(filename, pattern):
    lines = []
    with open(filename) as f:
        for line in f:
            if line.endswith(pattern):
                lines.append(line)
    return lines


def grep_cfg_any(filename, pattern):
    lines = []
    with open(filename) as f:
        for line in f:
            if pattern in line:
                lines.append(line)
    return lines


def grep_cfg(filename, pattern, start=False, end=False):
    if start:
        return grep_lines_start(filename, pattern)
    elif end:
        return grep_lines_end(filename, pattern)
    else:
        return grep_lines_any(filename, pattern)


result = grep_cfg("configs/config_r1.txt", "interface", start=True)
pprint(result)
# pprint(grep_cfg("configs/config_r1.txt", pattern="alias", start=True))

