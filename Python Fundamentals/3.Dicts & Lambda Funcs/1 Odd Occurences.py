# Odd_Occurrences

data_list = input().lower().split(" ")

occ_dict = {}

occ_dict = {word: data_list.count(word) for word in data_list}  # dictionary comprehension

occ_list = []

for key, value in occ_dict.items():
    if value % 2 == 1:
        occ_list.append(key)

print(", ".join(occ_list))
