#WAP to print even numbers in tuple

tup = (56,78,34,33,39,89,8)

for i in tup:
    if i % 2 == 0:
        print(i)


tup2=(45,[78,89],80,73,45,45,85)
print(tup2[0])
print(tup2[1])
print(tup2[1][0])
print(tup2[1][1])

tup2[1][0] = 45
print(tup2)


#WAP to count the 45 in the tuple
print(tup2.count(45))

# tuple can not be changed

#tup2[2]=78
#print(tup2)

