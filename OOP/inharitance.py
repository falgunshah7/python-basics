class Animal:
    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")


class Dog(Animal):
    def __init__(self, name="Dodo"):
        self.name = name
    def bark(self):
        print(f"My name is {self.name} and I can bark! woof woof!")

dog1 = Dog()
dog1.eat()
dog1.sleep()
dog1.bark()

dog2 = Dog('Max')
dog2.bark()