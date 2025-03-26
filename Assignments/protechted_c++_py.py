'''class Animal:
    def __init__(self, name):
        self._name = name  # Protected member

    def set_name(self, name):
        self._name = name

class Mammal(Animal):
    def display_mammal(self):
        print(f"Mammal Name: {self._name}")  # Accessing protected member

class Dog(Mammal):
    def bark(self):
        print(f"{self._name} says Woof!")  # Accessing protected member

# Main function
if __name__ == "__main__":
    my_dog = Dog("Buddy")

    my_dog.display_mammal()  # Works, accessing through class method
    my_dog.bark()
    print(my_dog._name)#you can access it in python otherwise you cant, so it not good to use it in python
    my_dog.set_name("Max")
    my_dog.display_mammal()  # Accessing after changing the name
'''

