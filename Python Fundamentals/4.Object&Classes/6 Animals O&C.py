#Animals

#Solution_1


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, number_of_legs: int):
        Animal.__init__(self, name, age)
        self.number_of_legs = number_of_legs

    def make_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}"


class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient: int):
        Animal.__init__(self, name, age)
        self.intelligence_quotient = intelligence_quotient

    def make_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}"


class Snake(Animal):
    def __init__(self, name, age, cruelty_coefficient: int):
        Animal.__init__(self, name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def make_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

    def __str__(self):
        return f"Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}"


data_list = input().split()
animals_list = []

while not data_list[0] == "I'm":
    if data_list[0] == "talk":
        name = data_list[1]
        current_animal = list(filter(lambda a: a.name == name, animals_list))[0]  # next(filter(lambda a: a.name == name, animals_list))
        print(current_animal.make_sound())
    else:
        kind = data_list[0]
        name = data_list[1]
        age = data_list[2]
        item = data_list[3]

        str_class_instance = f"{kind}(\"{name}\",{age}, {item})"

        current_animal = eval(str_class_instance)

        animals_list.append(current_animal)

    data_list = input().split()

        # if kind == "Dog":
        #     dog = Dog(name, age, item)
        #     animals_list.append(dog)
        # elif kind == "Cat":
        #     cat = Cat(name, age, item)
        #     animals_list.append(cat)
        # elif kind == "Snake":
        #     snake = Snake(name, age, item)
        #     animals_list.append(snake)

dogs_list = list(filter(lambda x: isinstance(x, Dog), animals_list)) #za da se podrediat kakto triabva
cats_list = list(filter(lambda x: isinstance(x, Cat), animals_list))
snakes_list = list(filter(lambda x: isinstance(x, Snake), animals_list))
sorted_animals = dogs_list + cats_list + snakes_list

for animal in sorted_animals:
    print(animal)

# #Solution_2
#
# class Dog:
#     def __init__(self, name, age, number_of_legs):
#         self.name = name
#         self.age = age
#         self.number_of_legs = number_of_legs
#
#     def produce_sound(self):
#         print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")
#
#
# class Cat:
#     def __init__(self, name, age, intelligence_quotient):
#         self.name = name
#         self.age = age
#         self.intelligence_quotient = intelligence_quotient
#
#     def produce_sound(self):
#         print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")
#
#
# class Snake:
#     def __init__(self, name, age, cruelty_coefficient):
#         self.name = name
#         self.age = age
#         self.cruelty_coefficient = cruelty_coefficient
#
#     def produce_sound(self):
#         print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")
#
#
# collection_dog = []
# collection_cat = []
# collection_snake = []
# command = input().split(' ')
# while not command[0] == "I'm":
#     if not command[0] == 'talk':
#         clas = command[0]
#         name = command[1]
#         age = int(command[2])
#         parameter = int(command[3])
#
#         if clas == 'Dog':
#             animal = Dog(name, age, parameter)
#             collection_dog.append(animal)
#         elif clas == 'Cat':
#             animal = Cat(name, age, parameter)
#             collection_cat.append(animal)
#         elif clas == 'Snake':
#             animal = Snake(name, age, parameter)
#             collection_snake.append(animal)
#     else:
#         for item in collection_dog:
#             if item.name == command[1]:
#                 item.produce_sound()
#         for item in collection_cat:
#             if item.name == command[1]:
#                 item.produce_sound()
#         for item in collection_snake:
#             if item.name == command[1]:
#                 item.produce_sound()
#     command = input().split(' ')
#
# for coll in collection_dog:
#     print(f'Dog: {coll.name}, Age: {coll.age}, Number Of Legs: {coll.number_of_legs}')
# for coll2 in collection_cat:
#     print(f'Cat: {coll2.name}, Age: {coll2.age}, IQ: {coll2.intelligence_quotient}')
# for coll3 in collection_snake:
#     print(f'Snake: {coll3.name}, Age: {coll3.age}, Cruelty: {coll3.cruelty_coefficient}')
#
#
# #Solution_3
#
# class Animal:
#     animals_list = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.animals_list.append(self)
#
#
# class Dog(Animal):
#     def __init__(self, name, age, number_of_legs):
#         super().__init__(name, age)
#         self.number_of_legs = number_of_legs
#
#     @staticmethod
#     def produce_sound():
#         return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
#
#
# class Cat(Animal):
#     def __init__(self, name, age, intelligence_quotient):
#         super().__init__(name, age)
#         self.intelligence_quotient = intelligence_quotient
#
#     @staticmethod
#     def produce_sound():
#         return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
#
#
# class Snake(Animal):
#     def __init__(self, name, age, cruelty_coefficient):
#         super().__init__(name, age)
#         self.cruelty_coefficient = cruelty_coefficient
#
#     @staticmethod
#     def produce_sound():
#         return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."
#
#
# def create_object(data):
#     cls, name, age, param = data
#     eval(cls)(name, int(age), int(param))
#
#
# def main():
#     data = input()
#     while data != "I'm your Huckleberry":
#         try:
#             create_object(data.split(' '))
#         except ValueError:
#             animal_name = data.split(' ')[1]
#             for animal in Animal.animals_list:
#                 # print(animal.__class__.__name__)   getting the class name of an instance
#                 if animal_name == animal.name:
#                     print(animal.produce_sound())
#         data = input()
#
#     for animal in Animal.animals_list:
#         if isinstance(animal, Dog):
#             print(f"Dog: {animal.name}, Age: {animal.age}, Number Of Legs: {animal.number_of_legs}")
#
#     for animal in Animal.animals_list:
#         if isinstance(animal, Cat):
#             print(f"Cat: {animal.name}, Age: {animal.age}, IQ: {animal.intelligence_quotient}")
#
#     for animal in Animal.animals_list:
#         if isinstance(animal, Snake):
#             print(f"Snake: {animal.name}, Age: {animal.age}, Cruelty: {animal.cruelty_coefficient}")
#
#
# if __name__ == '__main__':
#     main()