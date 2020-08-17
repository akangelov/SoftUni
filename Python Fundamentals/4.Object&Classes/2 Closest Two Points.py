#Closest_two_points

#Solution_1

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_info(self):
        return f"{self.x};{self.y}"


class Segment:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.distance = self.calc_distance()

    def calc_distance(self):
        side_a = abs(self.point_1.x - self.point_2.x)
        side_b = abs(self.point_1.y - self.point_2.y)
        side_c = math.sqrt(side_a ** 2 + side_b ** 2)
        return side_c

    def show_info(self):
        return f"{self.distance:.3f}\n({self.point_1.x}, {self.point_1.y})\n({self.point_2.x}, {self.point_2.y})"


def create_point(x, y):
    point = Point(x, y)
    return point


n = int(input())
points_list = []

for row in range(n):
    x, y = [int(num) for num in input().split()]
    point = create_point(x, y)
    points_list.append(point)

segment_list = []

for index_1 in range(len(points_list)):
    for index_2 in range(index_1 + 1, len(points_list)):
        segment = Segment(points_list[index_1], points_list[index_2])
        segment_list.append(segment)

for segment in sorted(segment_list, key=lambda s: s.distance):
    print(segment.show_info())
    break






