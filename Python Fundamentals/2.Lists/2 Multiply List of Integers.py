# Multiply_list_of_integers

data_list = input().split(" ")

p = int(input())

numbers_list = []

for el in data_list:
    numbers_list.append(int(el)*p)

print(*numbers_list)







