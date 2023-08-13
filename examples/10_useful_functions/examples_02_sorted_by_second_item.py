import operator


vlans = [('IT_VLAN', 320), ('Mngmt_VLAN', 99), ('User_VLAN', 1010), ('DB_VLAN', 11)]

def get_item_1(item):
    return item[1]


print(sorted(vlans, key=get_item_1))
print(sorted(vlans, key=operator.itemgetter(1)))


# new_vlans = [(vl_id, vl_name) for vl_name, vl_id in vlans]
# sorted_vlans = [(vl_name, vl_id) for vl_id, vl_name in sorted(new_vlans)]


vlans = {'IT_VLAN': 320, 'Mngmt_VLAN': 99, 'User_VLAN': 1010, 'DB_VLAN': 11}

# sorted(vlans)
# ['DB_VLAN', 'IT_VLAN', 'Mngmt_VLAN', 'User_VLAN']

# sorted(vlans.items())
# [('DB_VLAN', 11), ('IT_VLAN', 320), ('Mngmt_VLAN', 99), ('User_VLAN', 1010)]

print(sorted(vlans.items(), key=get_item_1))
print(sorted(vlans.items(), key=operator.itemgetter(1)))
# [('DB_VLAN', 11), ('Mngmt_VLAN', 99), ('IT_VLAN', 320), ('User_VLAN', 1010)]
