

vlans = ["1", "2", "3", "4", "5"]

vlans_int = []
# vlans_int = list()

for vl in vlans:
    vlans_int.append(int(vl))

print(vlans_int)



vlans = ["1", "2", "3", "4", "5"]

#vlans[0] = int(vlans[0])
#vlans[1] = int(vlans[1])
#vlans[2] = int(vlans[2])
#vlans[3] = int(vlans[3])
#vlans[4] = int(vlans[4])

index_range = range(len(vlans))

# for index in range(len(vlans)):
for index in index_range:
    vlans[index] = int(vlans[index])

print(vlans)
