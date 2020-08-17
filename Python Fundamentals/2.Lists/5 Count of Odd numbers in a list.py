#Count_of_odd_numbers_in_list

#Solution_1
num_list = list(map(int, input().split(" ")))

counter = 0

for num in num_list:
    if num % 2 != 0:
    #if not num % 2 == 0:
        counter += 1

print(counter)

#Solution_2
nums = list(map(int, input().split(" ")))

odd_nums_list = [num for num in nums if num % 2 == 1] #list comprehension
print(len(odd_nums_list))


