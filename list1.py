# List is a collection which is ordered and changeable.
# Allows duplicate members.

myList=["Oil","Soap",123,"Oil","kurkure","Dairy Milk"]
print(myList)
print(type(myList))
print(myList[0])

# Slicing list elements

print(myList[1:])
print(myList[2:5])

# you can use negative index as well

print(myList[-1])
print(myList[-2])

for i in myList:
    print(i,end=" ")
