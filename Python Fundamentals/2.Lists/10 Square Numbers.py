#Square_Numbers

#Solution_1
import math

nums = list(map(int, input().split(" ")))

result = []

for num in nums:
    if num < 0:
        nums.remove(num)

for num in nums:
    if int(math.sqrt(num)) == math.sqrt(num):
        result.append(num)

result.sort(reverse = True)

print(*result)

#Solution_2
from math import sqrt

def is_perfect_square(num):
    return int(sqrt(num)) == sqrt(num)

data_list = list(map(int, input().split(" ")))
list = []

for el in data_list:
    if is_perfect_square(el):
        list.append(el)

list.sort(reverse=True)
print(*list)

