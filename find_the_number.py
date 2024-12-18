#WAP to search particular element in list
n=int(input("Enter Number : "))
numbers=[10,85,36,54,8,15]

for i in numbers:
    if(i==n):
        print("element found : ",i)
        break
    else:
        print("Not Found : ",n)
        
    
