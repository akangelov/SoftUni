#Book_Shop

class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    @property
    def author(self):
        return self.__author

    @author.setter  #validacia
    def author(self, value: str):
        if len(value.split()) > 1:   #Proveriava dali ima 2 imena
            second_name = value.split()[1]
            if second_name[0].isdigit():
                raise Exception("Author not valid!")
        self.__author = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            raise Exception("Title not valid!")
        self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Price not valid!")
        self.__price = value

    def __str__(self):
        return f"Type: {self.__class__.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}"


class GoldenEditionBook(Book):
    def __init(self, title, author, price):
        Book.__init__(self, title, author, price)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Price not valid!")
        self.__price = value * 1.3

author = input()
title = input()
price = float(input())

try:
    book = Book(title=title, author=author, price=price)
    g_book = GoldenEditionBook(title=title, author=author, price=price)
    print(book)
    print() #prazen red
    print(g_book)
except Exception as ex:
    print(ex)








