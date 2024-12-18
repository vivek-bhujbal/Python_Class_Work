class Rectangle:
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

#Taking input from user
b=int(input("Enter Lenght : "))
h=int(input("Enter Breadth : "))

#creating an object of the rectangle class
rect = Rectangle(b,h)

#calling area method using rect object

print("Area of Rectangle is : ",rect.area())
