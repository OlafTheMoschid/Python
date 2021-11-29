class Rectangle:
    def __init__(self, x, y):
        if not (isinstance(x, (int, float)) and isinstance(x, (int, float))):
            raise TypeError("Type of x and y must be int or float")
        if x < 0 or y < 0:
            raise ValueError("x, y shouldn't be negative")

        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def get_perimeter(self):
        return 2 * (self.x + self.y)