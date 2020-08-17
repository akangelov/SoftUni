#Greater_of_two_Values

def compare_value(val_1, val_2):
    if val_1 < val_2:
        return val_2
    return val_1


if __name__ == "__main__":
    value_type = input()
    value_1 = input()
    value_2 = input()

    print(compare_value(value_1, value_2))