from pprint import pprint

r1 = {
    "IOS": "15.4",
    "IP": "10.255.0.1",
    "hostname": "london_r1",
    "location": "21 New Globe Walk",
    "Model": "4451",
    "Vendor": "Cisco",
}


nums_dict = {num: num * 10 for num in range(1, 6)}

# nums_dict = {}
# for num in range(1, 6):
#     nums_dict[num] = num * 10

r1_new = {key.lower(): value for key, value in r1.items()}

# r1_new = {}
# for key, value in r1.items():
# 	r1_new[key.lower()] = value
