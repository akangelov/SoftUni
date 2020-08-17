#Rectangle_Position

class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def is_inside(self, other_rect):
        if type(other_rect) is not type(self):
            raise TypeError('other_rect is not a Rectangle!')

        is_in_left = self.left >= other_rect.left
        is_in_right = self.right <= other_rect.right
        is_inside_horizontal = is_in_left and is_in_right

        is_in_top = self.top >= other_rect.top
        is_in_bottom = self.bottom <= other_rect.bottom
        is_inside_vertical = is_in_top and is_in_bottom

        return is_inside_horizontal and is_inside_vertical


def read_rectangle():
    coords = [int(num) for num in input().split(' ')]

    rect = Rectangle(*coords)
    return rect


rect1 = read_rectangle()
rect2 = read_rectangle()

print('Inside' if rect1.is_inside(rect2) else 'Not inside')


