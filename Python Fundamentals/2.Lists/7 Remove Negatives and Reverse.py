#Remove_Negatives_and_Reverse

#Solution_1

nums = list(map(int, input().split(" ")))

positive_nums = list(filter(lambda x: x > 0,nums))

positive_nums.reverse()

if positive_nums == []:
    print("empty")
else: print(*positive_nums)

#Solution_2

nums_list = list(map(int, input().split()))
positive_nums_list = list(filter(lambda num: num >= 0,nums_list))

if len(positive_nums_list) == 0:
    print("empty")
    exit(0) #alternativa na else:

print(*positive_nums_list[::-1])


#Solution_3

nums = list(map(int, input().split(" ")))

for el in nums:
    if el < 0:
        nums.remove(el)

nums.reverse()

if nums == []:
    print("empty")
else:print(*nums)









