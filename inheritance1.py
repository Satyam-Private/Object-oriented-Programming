# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!" 
    


# Creating an instance of Dog
dog = Dog("tiger")

print(dog.speak())  

