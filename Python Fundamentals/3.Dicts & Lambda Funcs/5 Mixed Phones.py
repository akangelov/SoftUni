# Mixed_Phones

data_list = input().split(" : ")

tel_book = {}

while not data_list[0] == "Over":
    if data_list[1].isdigit():
        key = data_list[0]
        value = data_list[1]
        tel_book[key] = value
    else:
        key = data_list[1]
        value = data_list[0]
        tel_book[key] = value
    data_list = input().split(" : ")

for key, value in sorted(tel_book.items()):
    print(f"{key} -> {value}")



