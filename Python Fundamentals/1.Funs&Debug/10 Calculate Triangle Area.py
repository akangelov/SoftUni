#Calculate_Triangle_Area

#area = Hb*b/2


def calc_triangle_area(side, height):
    return side * height / 2


if __name__ == "__main__":
    side = float(input())
    height = float(input())
    print(calc_triangle_area(side, height))
