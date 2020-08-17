# Shellbound

#Solution_1

import math as m

regions = dict()

while True:
    parts = [x for x in input().split(" ") if x]
    if parts[0] == "Aggregate":
        break
    region = parts[0]
    shell = int(parts[1])

    if regions.__contains__(region):
        if shell not in regions[region] :
            regions[region].append(shell)
    else:
        regions.__setitem__(region,[])
        regions[region].append(shell)

seperator = ", "
for region in regions:
    sumOfShells = sum(regions[region]) - (sum(regions[region]) // len(regions[region]))
    if len(regions[region]) == 1:
        print(f"{region} -> {seperator.join(str(item) for item in regions[region])} ({regions[region][0]})")
    else:
        print(f"{region} -> {seperator.join(str(item) for item in regions[region])} ({sumOfShells})")

#Solution_2

import math

vladi = {}
data = input().split(" ")

while not data[0] == "Aggregate":
    region = data[0]
    shell = data[1]

    if not region in vladi:
        vladi[region] = shell  #vladi[key] = value
    else:
        if shell in vladi[region]:
            data = input().split(" ")
            continue
        else:
            vladi[region] = vladi[region] + ", " + shell

    data = input().split(" ")

count = 0
for key, value in vladi.items():
    count = 0
    sum = 0
    a = value.split(", ")
    for el in a:
        elem = int(el)
        sum += elem
        count += 1
    giant = sum - sum / count
    print(f"{key} -> {value} ({math.ceil(giant)}) ")




