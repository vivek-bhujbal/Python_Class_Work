#WAP Find Maximum of Two Number

list1=[98,52,95,89,64]

new_list = max(list1)
s = sorted(set(list1))[-2]

print("First Largest Number is : ",new_list)
print("Second Largest Number is : ",s)

