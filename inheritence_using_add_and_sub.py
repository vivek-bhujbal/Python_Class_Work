class Number:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

class Sum(Number):
    def sums(self):
        return self.num1 + self.num2

class Sub(Number):
    def subs(self):
        return self.num1 - self.num2

    
num1=int(input("Enter Number : "))
num2=int(input("Enter Number : "))

s=Sum(num1,num2)
su=Sub(num1,num2)

print(s.sums())
print(su.subs())
