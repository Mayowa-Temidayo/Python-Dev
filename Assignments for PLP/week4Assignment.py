#OOP IN PYTHON
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Mayowa", 33, "male")

# Calling the introduce method to display the person's information
person1.introduce()

#THE OUTPUT

#Hello, my name is Mayowa. I am 33 years old and I am male.
