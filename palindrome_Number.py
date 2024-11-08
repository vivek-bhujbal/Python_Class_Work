n=int(input("Enter any Number : "))
n1=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(n1==rev):
    print("This Number is Palindrome : ",rev)
else:
    print("This Number is Not Palindrome : ",rev)
