class Test:
    def add(self,a,b):
        res=a+b
        return res

    def sub(self,a,b):
        res=a-b
        print("Substraction is : ",res)

    def mul(self,a,b):
        res=a*b
        print("Multiplication is : ",res)

    def div(self,a,b):
        res=a/b
        print("Division is : ",res)

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

T = Test()
answer = T.add(a,b)
print("The addition of two numbers are : ",answer)
T.sub(a,b)
T.mul(a,b)
T.div(a,b)
