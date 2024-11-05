#create a class called person,that has three attributes,name,age and gender
#then create a constructore method and method and object

# Define the Person class
class Person:
    # Constructor to initialize name, age, and gender
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to display person details
    def display_info(self):
        print(f"my name is {self.name} i am {self.age} years old and {self.gender}")


# Create an object of the Person class
person1 = Person("Francis", 22, "Male")

# Output the details of the person object
person1.display_info()
