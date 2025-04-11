# Exercise 1: Basic Class Definition
# Define a basic class called Animal with a method called make_sound that prints a sound.

# Create an instance of Animal and call the make_sound method
class Animal:
    def __init__(self, sound):
        self.sound = sound
    def __str__(self):
        return f"The animal makes a sound!"
make_sound = Animal("The animal makes a sound")
print(make_sound)




# Exercise 2: Inheritance
# Create a subclass of Animal called Dog that overrides the make_sound method.

# Create an instance of Dog and call the make_sound method.


class dog(Animal):
    def __init__(self, sound ):
        self.sound = sound
    def __str__(self):
        return f"WOOF! WOOF!"
noise = dog("WOOF! WOOF!")
print(noise)


# Exercise 3: Adding Attributes
# Add an attribute to the Animal class and initialize it through the constructor.

# Update the Dog class to use the new attribute and update the make_sound method to use the attribute.

# Create an instance of Dog with a name and call the make_sound method.
