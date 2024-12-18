'''import random   #importing random module to generate random numbers

# Guess The Number
for i in range(1,11):
    Number = random.randint(1,10)

    x=int(input("Enter The Number : "))
    if(x==Number):
        print("WOW..!!!,You Won the Match")
        print("You Guess The Number is Right : ",Number)
        break
    else:
        print("You have only 2 chance")
    

    y=int(input("Enter the Number : "))
    if(y==Number):
        print("WOW..!!!,You Won the Match")
        print("You Guess The Number is Right : ",Number)
        break
    else:
        print("You have only 1 chance")
        

    z=int(input("Enter the Number : "))
    if(z==Number):
        print("WOW..!!!,You Won the Match")
        print("You Guess The Number is Right : ",Number)
        break
    else:
        print("You Lost the Game...")
        print("You Guess The Number is Wrong the right number is : ",Number)
        break
'''

'''import random
    
Number = random.randint(1,10)

num=int(input("Enter Number : "))
i=0
while i < num:
    i = i + 1

if(Number==i):
    print("Cpngratulations! guess number is : ",Number)
else:
    print("Guess Again")
'''
import random

# Generate a random number between 0 and 20
num = random.randint(1,10)


print("Enter number between 1 and 10")

# Start the guessing loop
while True:
    # Ask for user input
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is correct
    if guess == num:
        print("Congratulations!")
        break
    else:
        print("Guess Again")

            


