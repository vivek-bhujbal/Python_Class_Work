#WAP to print table using function

n=int(input("Enter any Number : "))

def table(n):
    for i in range(1,11):
        tab=i*n
        print(tab)
table(n)
