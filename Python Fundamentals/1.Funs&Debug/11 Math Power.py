#Math_Power


def raise_to_power(number, power):
    return number ** power

    # result = 1;
    # for i in range(power)
    # result *= number
    # return result


if __name__ == "__main__":
    number = int(input())
    power = int(input())
    print(raise_to_power(number, power))