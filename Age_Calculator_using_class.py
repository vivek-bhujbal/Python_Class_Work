from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age = age - 1
        return age

    def __str__(self):
        return f"Name: {self.name}\nCountry: {self.country}\nAge: {self.calculate_age()}"

# Example usage
if __name__ == "__main__":
    person = Person("Vivek", "India", "2004-12-25")
    print(person)
    print(f"\n{person.name} is {person.calculate_age()} years old.")
