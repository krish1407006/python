# operator overloading in python


class point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return point((self.x + other.x),(self.y + other.y))

p1 = point(2,3)
p2 = point(4,5)

p3 = p1 + p2  # this will call the __add__ method of the point class


print("p1:",p1.x,p1.y)
print("p2:",p2.x,p2.y)

print("p3:",p3.x,p3.y)


