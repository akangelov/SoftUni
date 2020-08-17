#Rotate_a_list_of_strings

#Solution_1

data_list = input().split(" ")
print(data_list[-1], end=" ") #prints on the same line the two lines. first print prints the last element  
print(*data_list[:-1])        #the second prints all elements after the first


#Solution_2

data_list = input().split(" ")

list_of_str = []

for el in data_list:
    list_of_str.append(el)

a = list_of_str.pop()

list_of_str.insert(0,a)

print(*list_of_str)

