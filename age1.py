from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def calculate_age(self):
        
        today = datetime.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

    def __str__(self):
        return f"Name: {self.name}\n, Country: {self.country}\n, Age: {self.calculate_age()}"


if __name__ == "__main__":
    person = Person("Vivek","India",2004-12-25)
    print(person)
    print(f"{person.name} is {person.calculate_age()} years old.")
