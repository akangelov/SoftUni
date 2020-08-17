#Count_numbers

#Solution 1

data = list(map(int, input().split(" ")))
data.sort()

num = -1
for element in data:
    if not num == element:
        data.count(element)
        print(f"{element} -> {data.count(element)}")
        num = element

#Solution_2

my_list = list(map(int, input().split(' ')))
a_list = my_list
list1 = sorted(my_list)
a_list = sorted(a_list)
counter = 0
a_list = list(dict.fromkeys(a_list))

for num in a_list:
    counter = 0
    for num1 in list1:
        if num == num1 and counter == 0:
            list1.count(num)
            counter += 1
            print(f'{num} -> {list1.count(num)}')