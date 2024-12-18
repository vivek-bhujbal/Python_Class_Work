class Average:
    def avg(self,a,b,c):
        res=(a+b+c)/3
        print("Average is : ",res)


a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))

A=Average()
A.avg(a,b,c)
