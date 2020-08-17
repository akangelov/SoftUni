#Split_by_word_casing

#Solution_1

import re


def IsLowerCase(word):
    if re.findall(r"^[a-z]+$", word):
        return True
    return False


def IsUpperCase(word):
    if re.findall(r"^[A-Z]+$", word):
        return True
    return False


sentence = input()
regex = r"[^[,;:.!()\"\'\\\/[\] ]+"
matches = re.findall(regex, sentence)

lowerCaseArr = []
mixedCaseArr = []
upperCaseArr = []

for word in matches:
    if IsLowerCase(word):
        lowerCaseArr.append(word)
    elif IsUpperCase(word):
        upperCaseArr.append(word)
    else:
        mixedCaseArr.append(word)

seperator = ", "
print(f"Lower-case: {seperator.join(lowerCaseArr)}")
print(f"Mixed-case: {seperator.join(mixedCaseArr)}")
print(f"Upper-case: {seperator.join(upperCaseArr)}")


#Solition_2

import re

input = input()

data = re.split("[\,\;\:\.\!\(\)\"\'\\\/\[\]\ ]+", input)
lower = []
mixed = []
upper = []

for element in data :
    if element == "" :
        continue

    lower_count = 0
    upper_count = 0
    mixed_count = 0

    for letter in element :
        lower_count += letter.islower()
        upper_count += letter.isupper()

    if len(element) == lower_count :
        lower.append(element)
    elif len(element) == upper_count :
        upper.append(element)
    else :
        mixed.append(element)

print('Lower-case: ', end="")
print(*lower, sep=", ")
print('Mixed-case: ', end="")
print(*mixed, sep=", ")
print('Upper-case: ', end="")
print(*upper, sep=", ")


#Solution_3

import re

input = input()

data = re.split("[\,\;\:\.\!\(\)\"\'\\\/\[\]\ ]+", input)
lower = []
mixed = []
upper = []

for element in data:
    if element == "":
        continue
    lower_count = 0
    upper_count = 0
    mixed_count = 0
    for letters in element:
        letter = ord(letters)

        if letter >= 97 and letter <= 122:
            lower_count += 1
        elif letter >= 65 and letter <= 90:
            upper_count += 1
        else:
            mixed_count += 1

    if upper_count == 0 and mixed_count == 0:
        lower.append(element)
    elif lower_count == 0 and mixed_count == 0:
        upper.append(element)
    else:
        mixed.append(element)

print(f'Lower-case: ', end="")
print(*lower, sep=", ")
print(f'Mixed-case: ', end="")
print(*mixed, sep=", ")
print(f'Upper-case: ', end="")
print(*upper, sep=", ")


#Solution_4

import re

words = [str(item) for item in re.split("[,;:.!()\"\'\\\\/\[\] ]+", input()) if item != ""]

lower_case = []
upper_case = []
mixed_case = []

for word in words:
    if word.islower():
        checker = True
        for letter in word:
            if 97 <= ord(letter) <= 122:
                checker = True
            else:
                checker = False
                break
        if checker:
            lower_case += [word]
        else:
            mixed_case += [word]

    elif word.isupper():
        checker = True
        for letter in word:
            if 65 <= ord(letter) <= 90:
                checker = True
            else:
                checker = False
                break
        if checker:
            upper_case += [word]
        else:
            mixed_case += [word]
    else:
        mixed_case += [word]

print(f"Lower-case: ", end="")
print(", ".join(lower_case))
print(f"Mixed-case: ", end="")
print(", ".join(mixed_case))
print(f"Upper-case: ", end="")
print(", ".join(upper_case))