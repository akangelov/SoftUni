#Sum_adjacent_equal_numbers

nums_list = list(map(float, input().split()))
length = len(nums_list) - 1
index = 0

while index < len(nums_list) - 1:
    if nums_list[index] == nums_list[index + 1]:
        current_sum = nums_list[index] + nums_list[index + 1]
        del nums_list[index + 1]
        nums_list[index] = current_sum
        index = -1
    index += 1

print(*nums_list)