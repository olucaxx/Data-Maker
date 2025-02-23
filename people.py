import name, age, phone_number

class People:
    def __init__(self):
        self.name = name.generate_random_name(compound=True)
        self.age = age.generate_random_age()
        self.phone_number = phone_number.generate_random_number()
        
    def __str__(self):
        return f"{self.name}, {self.age}, {self.phone_number}"
 
amount = 15 

people = [People() for x in range(amount)]

for person in people:
    print(person)