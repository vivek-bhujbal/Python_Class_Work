class  Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark")

    def DogInfo(self):
        print(self.name," is ", str(self.age)," years old")
d=Dog("puppy",5)
d.DogInfo()
d.bark()
