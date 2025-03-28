# Exercise 1: Create a class called `Person` that has the following attributes:
# - name (string)
# - age (integer)
# - email (string)
# The class should have a method called `introduce` that prints a message introducing the person.

class person:

    def_init(self):
        self.name = 'Vincent'
        self.age = 13
        self.email = 'vincewat5000@gmail.com'  
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and my email is{self.email}.")
        

my_object = person


my_object.introduce()
