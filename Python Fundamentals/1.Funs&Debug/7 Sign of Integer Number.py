#Sign_of_Integer_Number


def define_sign(n):
    if n < 0:
        return f"The number {n} is negative."
    elif n == 0:
        return f"The number {n} is zero."
    else:
        return f"The number {n} is positive."


if __name__ == "__main__":
    number = int(input())
    result = define_sign(number)
    print(result)
