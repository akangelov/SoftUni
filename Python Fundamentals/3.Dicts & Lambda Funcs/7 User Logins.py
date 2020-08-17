# User_Logins

#Solution_1

data_list = input().split(" -> ")

passwords = {}

while not data_list[0] == "login":
    key = data_list[0]
    value = data_list[1]
    passwords[key] = value
    data_list = input().split(" -> ")

login = input().split(" -> ")

counter = 0

while not login[0] == "end":
    new_key = login[0]
    new_value = login[1]
    if new_key not in passwords.keys():
        print(f"{new_key}: login failed")
        counter += 1
    elif new_value not in passwords.values():
        print(f"{new_key}: login failed")
        counter += 1
    else:
        print(f"{new_key}: logged in successfully")
    login = input().split(" -> ")

print(f"unsuccessful login attempts: {counter}")


#Solution_2

name_pass = {}

counter = 0

while True:
    command = [item for item in input().split(" -> ")]
    if "login" in command:
        break
    name_pass[command[0]] = command[1]
while True:
    command = [item for item in input().split(" -> ")]
    if "end" in command:
        break
    if command[0] in name_pass and name_pass.__getitem__(command[0]) == command[1]:
        print(f"{command[0]}: logged in successfully")
    else:
        print(f"{command[0]}: login failed")
        counter += 1

print(f"unsuccessful login attempts: {counter}")

#Solution_3

import re

ptrn = re.compile('\\s+->\\s+')
logins = {} # (usr, psw)

while True :
    inp_list = re.split(ptrn, input())
    usr = inp_list[0]
    if usr == 'login' :
        break
    logins[usr] = inp_list[1]

cnt = 0
while True :
    inp_list = re.split(ptrn, input())
    usr = inp_list[0]
    if usr == 'end' :
        break
    psw = inp_list[1]
    if not usr in logins.keys() :
        print(f'{usr}: login failed')
        cnt += 1
        continue
    if psw != logins[usr] :
        print(f'{usr}: login failed')
        cnt += 1
        continue
    print(f'{usr}: logged in successfully')

print(f'unsuccessful login attempts: {cnt}')


#Solution_4

command = input()
name_dict = {}
counter = 0

while not command == 'login':
    data = [item for item in command.split(" -> ")]
    name_dict[data[0]] = data[1]
    command = input()

command = input()

while not command == "end":
    # data_2 = [item for item in command.split(" -> ")]
    key, value = command.split(" -> ")
    if key in name_dict:
        if value == name_dict[key]:
            print(f"{key}: logged in successfully")
        else:
            print(f"{key}: login failed")
            counter += 1
    else:
        print(f"{key}: login failed")
        counter += 1
    command = input()

print(f"unsuccessful login attempts: {counter}")















