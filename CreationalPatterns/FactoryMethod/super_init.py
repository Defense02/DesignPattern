class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # calls Animal.__init__(self, name)
        self.breed = breed
        print(f"Dog created: {self.name}, Breed: {self.breed}")

dog = Dog(toby, baby)