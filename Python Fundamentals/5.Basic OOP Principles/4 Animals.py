#Animals

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise Exception("Invalid Input")
        self.age = value

    @abstractmethod #vsichki po dolu klasove go implementirat
    def produce_sound(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}\n"


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Woof!"


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Ribbit"


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Meow"

class TomCat(Cat):
    def __init__(self, name, age, gender="Male"): #default value Male, ako ne e shte se prezapishe
        Cat.__init__(self, name, age, gender="Male")
        self.gender = "Male"

    def produce_sound(self):
        return "MEOW"

class Kitten(Cat):
    def __init__(self, name, age, gender="Female"): #default value Male, ako ne e shte se prezapishe
        Cat.__init__(self, name, age, gender="Female")
        self.gender = "Female"

    def produce_sound(self):
        return "MEOW"

animals_list = []

while True:
    kind = input()
    if kind == "Beast!":
        break

    name, age, gender = input().split()
    obj_str = f"{kind}(\"{name}\",{int(age)},\{gender}\")"
    try:
        obj = eval(obj_str)
        animals_list.append(obj)
    except Exception as ex:
        print("Invalid input!")

for animal in animals_list:
    print(animal)





