from pprint import pprint


def grep_lines_start(lines, pattern):
    lines = []
    for line in lines:
        if line.startswith(pattern):
            lines.append(line)
    return lines


def grep_lines_end(lines, pattern):
    lines = []
    for line in lines:
        if line.endswith(pattern):
            lines.append(line)
    return lines


def grep_cfg_any(lines, pattern):
    lines = []
    for line in lines:
        if pattern in line:
            lines.append(line)
    return lines


def grep_cfg(filename, pattern, start=False, end=False):
    with open(filename) as f:
        if start:
            return grep_lines_start(f, pattern)
        elif end:
            return grep_lines_end(f, pattern)
        else:
            return grep_lines_any(f, pattern)


result = grep_cfg("configs/config_r1.txt", "interface", start=True)
pprint(result)
# pprint(grep_cfg("configs/config_r1.txt", pattern="alias", start=True))

