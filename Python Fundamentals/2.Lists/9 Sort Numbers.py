#Sort_Numbers

nums = list(map(int, input().split(" ")))

nums.sort()

a_list = list(map(str, nums))

print(" <= ".join(a_list))

