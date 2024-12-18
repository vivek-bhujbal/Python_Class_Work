class Area:
    def __init__(self,l,b):
        self.l = l
        self.b = b

class Rectangle(Area):
    def rect(self):
        return self.l * self.b

class Traingle(Area):
    def tra(self):
        return 1/2 * self.l * self.b

l=int(input("Enter Lenght : "))
b=int(input("Enter Breadth : "))

r=Rectangle(l,b)
t=Traingle(l,b)
print("Area of Rectangle is : ",r.rect())
print("Area of Traingle is : ",t.tra())


