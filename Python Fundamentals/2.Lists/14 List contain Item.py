#List_contains_item

nums = list(map(int,input().split(" ")))

a = int(input())

for num in nums:
    if num == a:
        print("yes")
        break

else : print("no")

