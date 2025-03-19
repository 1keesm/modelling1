from point import Point
import random

class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)):
            #raise TypeError("x must be a number") #raise --> raises an exception from your own condition
            raise PointException("x must be a number") #--> we can create our own exceptions
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y) #replaces the self.x=x and self.y=y from similar class in point
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1,2, "red")

print(p.distance_orig())
print(p)
# color_points = []
# colors = ["red", "green", "blue", "yellow", "magenta", "black", "periwinkle", "white", "cyan", "burgundy"]
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10,10),
#                    random.randint(-10,10),
#                    random.choice(colors)))
#
# print(color_points)
# color_points.sort()
# print(color_points)