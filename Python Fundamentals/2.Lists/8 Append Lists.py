#Append_Lists
#Solution_1
inp = input().split('|')
inp.reverse()
res = []

for s in inp :
    s = s.split()
    res += s

print(*res)

#Solution_2
data_list = input().split("|")
data_list.reverse()
new_list = []

for el in data_list:
    new_list.append(el)

final_list = ' '.join(new_list).split()
print(*final_list)
