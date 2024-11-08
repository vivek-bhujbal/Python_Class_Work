#use the break statement

for i in range(1,21):
    if(i==10):
        break
    print(i)

print("------------||-----------")

#use the continue statement
for i in range(1,21):
    if(i==10):
        print("skipped")
        continue
    print(i)
