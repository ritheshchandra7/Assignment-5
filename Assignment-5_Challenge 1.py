#Square Numbers and Return Their Sum
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return(a + b + c)


result = Point(1, 3, 5)
print(result.sqSum())