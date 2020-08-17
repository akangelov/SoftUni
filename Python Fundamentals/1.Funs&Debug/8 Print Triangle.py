#Print_Triangle


def print_line(start, end):
    for i in range(start, end+1):
        print(i, end=" ") #end=" " is printing on the same row
    print() #get on the next row


def print_triangle(n):
    for i in range(1, n):
        print_line(1, i)
    for i in range(n, 0, -1):
        print_line(1, i)


if __name__ == "__main__":
    number = int(input())
    print_triangle(number)