# Count_Real_Numbers

numbers_list = list(map(float, input().split(" ")))

occ_dict = {num: numbers_list.count(num) for num in numbers_list} #List comprehension

for key,value in sorted(occ_dict.items()):
    print(f"{key} -> {value} times")






