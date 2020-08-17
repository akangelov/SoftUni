#Smallest_item_in_list

#Solution_1
nums = list(map(int,input().split(" ")))

min_number = nums[0]

for el in nums:
    if el < min_number:
        min_number = el

print(min_number)

#Solution_2
nums = list(map(int,input().split(" ")))

print(min(nums))

#Solution_3
nums = list(map(int, input().split(" ")))

nums.sort()

print(nums[0])


