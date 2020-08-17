# Letter_Repetition

char_list = input()

occ_dict = dict.fromkeys(char_list, 0) #fromkeys pravi novo dictionary ot char_list i assign-va za value 0

for i in char_list:
    occ_dict[i] += 1

for key,value in occ_dict.items():
    print(f"{key} -> {value}")





