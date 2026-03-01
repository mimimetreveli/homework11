class point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

point1=point(3,5)
point2=point(4,5)
print(point1)
print(point2)