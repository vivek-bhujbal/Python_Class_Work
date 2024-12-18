l1=[67,76,89,67]
remove_dup=list(set(l1))
print("The final list is : ",remove_dup)
print(remove_dup)


sorted_list = sorted(remove_dup)

print("The Sorted elements in list : ",sorted_list)

second_largest = sorted_list[-2]
print("Second Largest Number is : ",second_largest)
