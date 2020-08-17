#Dict_Ref_Advanced

data_list = input().split(" -> ")

names_dict = {}

while not data_list[0] == 'end':
    name = data_list[0]
    item = data_list[1].split(', ')

    if (len(item) == 1 and item[0].isdigit()) or len(item) > 1:
        if name not in names_dict.keys():
            names_dict[name] = []
        names_dict[name].extend(item)
    else:
        if item[0] in names_dict.keys():
            names_dict[name] = []
            names_dict[name].extend(names_dict[item[0]])

    data_list = input().split(" -> ")

for item in names_dict.items():
    print(f"{item[0]} === {', '.join(item[1])}")