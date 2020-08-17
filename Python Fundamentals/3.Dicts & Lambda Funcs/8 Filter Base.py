#Filter_base

#Solution_1

data_list = input().split(" -> ")

dict_age = {}
dict_sal = {}
dict_pos = {}

while not data_list[0] == "filter base":
    if  data_list[1].isdigit():
        key = data_list[0]
        value = data_list[1]
        dict_age[key] = value
    elif "." in data_list[1]:
        key = data_list[0]
        value = data_list[1]
        dict_sal[key] = value
    else:
         key = data_list[0]
         value = data_list[1]
         dict_pos[key] = value
    data_list = input().split(" -> ")

info = input()

if info == "Age":
    for key, value in dict_age.items():
        print(f"Name: {key}\nAge: {value}\n====================")
elif info == "Salary":
    for key, value in dict_sal.items():
        print(f"Name: {key}\nSalary: {value}\n====================")
elif info == "Position":
    for key, value in dict_pos.items():
        print(f"Name: {key}\nPosition: {value}\n====================")

#Solution_2

        age = dict()
        salary = dict()
        position = dict()

        filterType = ""
        while True:
            string = input()
            if string == "filter base":
                filterType = input()
                break

            parts = string.split(" -> ")
            key = parts[0]
            value = parts[1]

            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                    if int(value) == float(value):
                        value = int(value)
                except ValueError:
                    value

            if type(value) == int:
                age.__setitem__(key, value)
            elif type(value) == float:
                salary.__setitem__(key, value)
            else:
                position.__setitem__(key, value)

        result = None
        if filterType == "Position":
            result = position
        elif filterType == "Age":
            result = age
        else:
            result = salary

        for key in result:
            print(f"Name: {key}")
            print(f"{filterType}: {result[key]}")
            print(20 * "=")






