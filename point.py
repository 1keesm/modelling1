import random

class Point:
    def __init__(self, x, y):
        """

        :param x: the x axis position
        :param y: the y axis position
        """
        self.x = x #defines x attribute via self.x
        self.y = y #and assign the value of x to it

    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x,y>
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__() #use the same way if printing as str

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance

if __name__ == "__main__":
    #Now we need ot instantiate it!
    p = Point(1, 2)#p is an instance of 1 and 2
    p2 = Point(3,4)
    print(p.x, p.y)
    print(p2.x, p2.y)
    print(f"p.x = {p.x} and p.y = {p.y}")
    print(f"p2.x = {p2.x} and p2.y = {p2.y}")
    p.x = 20
    print(f"p.x = {p.x}")
    print(p)
    # create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10,10),#x value
                            random.randint(-10,10))) #y value

    print("i got these random 5 points")
    for p in points:
        print(p)
    print(points)

    #the final purpose is to sort the list of random points


    p = Point(3,4)
    print(p.distance_orig())#expect 5 answer
    p2 = Point(1,1)
    print(f"I am comparing p and p2: {p > p2}")

    print("The sorted list of points is")
    points.sort()
    print(points)