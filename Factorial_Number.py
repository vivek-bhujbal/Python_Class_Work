num = int(input("Enter The Number : "))
fact=1
ori_num = num

while num > 1:
    fact = fact * num
    num = num - 1
print("Factorial Number : ",fact)

'''for i in range(num):
    if(i>0):
        num=num * i

print("Factorial Number is : ",num)'''


'''
5! = 5*4*3*2*1=120

iteration 1:num=5 5>1 True
    fact=fact*num
iteration 2:num=4 4>1 True
    fact=5*4=20
iteration 3:num=3 3>1 True
    fact=20*3=60
iteration 4:num=2 2>1 True
    fact=60*2=120
iteration 5:num=1 1>1 False

Then Factorial is = 120
'''
    

    
