# Classes
# A programmatic object containing data and methods
# i.e variable and functions


# Basic Form

"""
class Classname:

    attribute = "some data"

    def methodname(input):
        <code for method goes here>
        return value
"""

class Dog:

    breed = "labrador"
    weight = 20
    energy = "Medium"

    def communicate(self):
       return "woof"


goldie = Dog()

print(goldie.breed)
print(goldie.communicate())


bonnie = Dog()

bonnie.energy = "High"

print(bonnie.energy)
print(bonnie.breed)
print(bonnie.communicate())



