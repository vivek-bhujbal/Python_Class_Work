#WAP to check whether person can vote or not using function

n=int(input("Enter Number : "))

def age(n):
    if n >= 18:
        print("You are eligible")
    else:
        print("You are not eligible")
age(n)
