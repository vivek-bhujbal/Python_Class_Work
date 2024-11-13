#WAP to get area of rectangle

l=float(input("Enter Lenght : "))
w=float(input("Enter Width : "))

def area(l,w):
    a=l*w
    return a
area_rect=area(l,w)
print("Area of Rectangle is : ",area_rect)
