
words = ['id', 'name', 'IT_VLAN', 'Mngmt_VLAN', 'to_name', 'port']

print(sorted(words))


def lower(string):
    print(f"{string=}")
    return str(string).lower()



print(sorted(words, key=lower))
# print(sorted(words, key=str.lower))
