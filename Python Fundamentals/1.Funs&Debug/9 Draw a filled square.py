#Draw_a_Filled_Square


def print_header_row(n):
    print('-' * 2 * n)


def print_middle_row(n):
    print('-', end='') #end meaning here stay on the same row
    for i in range(n - 1):
        print("\\/", end='')
    print('-')

if __name__ == "__main__":
    number = int(input())
    print_header_row(number)
    for i in range(number - 2):
        print_middle_row(number)
    print_header_row(number)

