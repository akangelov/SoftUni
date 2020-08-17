#Distance_between_points

#Solution_1
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(point_1: Point, point_2: Point):
    side_a = abs(point_1.x - point_2.x)
    side_b = abs(point_1.y - point_2.y)
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    return side_c


def create_point(x, y):
    point = Point(x, y)
    return point


x_1, y_1 = list(map(int, input().split()))
x_2, y_2 = list(map(int, input().split()))

point_1 = create_point(x_1, y_1)
point_2 = create_point(x_2, y_2)

distance = calc_distance(point_1, point_2)
print(f"{distance:.3f}")

