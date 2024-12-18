import random   #importing random module to generate random numbers

# Simulating temperature readings
for i in range(1,11):   # 10 temperature readings
    temperature = random.randint(20,100)
    print(f"Reading {i} : Temprature = {temperature} C")

    if temperature > 70:
        print("Danger! High temperature detected. Stoping monitoring.")
        break
