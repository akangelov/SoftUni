# Wardrobe

#Solution_1

n = int(input())

wardrobe_dict = {}

for iteration in range(n):
    data_list = input().split(' -> ')
    color = data_list[0]
    clothes = data_list[1].split(',')

    if color not in wardrobe_dict.keys():
        wardrobe_dict[color] = []

    wardrobe_dict[color].extend(clothes)

items_count_dict = {}

for color, clothes_list in wardrobe_dict.items():
    items_count_dict[color] = \
        {garment: clothes_list.count(garment)
         for garment in clothes_list}

data_list = input().split()
color_to_be_found = data_list[0]
clothes_to_be_found = data_list[1]

for color, kvp in items_count_dict.items():
    print(f"{color} clothes:")
    for garment, garment_count in kvp.items():
        if color_to_be_found == color and clothes_to_be_found == garment:
            print(f"* {garment} - {garment_count} (found!)")
        else:
            print(f"* {garment} - {garment_count}")

#Solution_2

# Dictionaries inside a dictionary
def solve():
    n = int(input())
    dic = dict()

    for colours in range(n):
        lst = input().split(' -> ')
        color = lst[0]
        clothes = lst[1].split(',')

        if color not in dic.keys():
            dic[color] = dict()
        for cloth in clothes:
            if cloth not in dic[color].keys():
                dic[color][cloth] = 1
            else:
                dic[color][cloth] += 1          # ex: {Blue: {cloth: += 1} }

    wanted_clothes = input().split()
    wanted_color = wanted_clothes[0]
    wanted_cloth = wanted_clothes[1]
    match = "(found!)"

    for key, value in dic.items():
        # print(value)               # ex: {'hat': 1, 'dress': 1, 't-shirt': 1, 'boxers': 1}
        # print(value.keys())        # ex: dict_keys(['hat', 'dress', 't-shirt', 'boxers'])
        print(f"{key} clothes:")     # first key: Red, Blue....
        for item in value.keys():    # entering the inner keys
            # print(item)            # ex: hat, dress, t-shirt (all one by one)
            if wanted_color == key and wanted_cloth == item:
                print(f"* {item} - {dic[key][item]} {match}")
            else:
                print(f"* {item} - {dic[key][item]}")


if __name__ == '__main__':
    solve()

