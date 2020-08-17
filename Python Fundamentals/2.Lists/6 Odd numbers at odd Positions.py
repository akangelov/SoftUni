#Odd_numbers_at_odd_positions

#Solution_1
nums = list(map(int, input().split(" ")))

for index, value in enumerate(nums):
    if index % 2 == 1 and value % 2 == 1:
        print(f"Index {index} -> {value}")

#Solution_2
nums = [int(item) for item in input().split(" ")]
counter = 0
for item in nums:
    if counter % 2 != 0:
        if item % 2 != 0:
            print(f"Index {counter} -> {item}")
    counter += 1

# num_list = list(map(int, input().split(" ")))
#
# for i in num_list:
#     if num_list[i] % 2 != 0 and num_list.index(i) % 2 != 0:
#         print(f"Index {i} -> {i}")

