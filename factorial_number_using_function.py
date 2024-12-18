#WAP to get factorial of number using function

n=int(input("Enter Number : "))
ans=1
def factorial(n):
    for i in range(n):
        if i > 0:
            n=n*i
    print(n)     
factorial(n)
