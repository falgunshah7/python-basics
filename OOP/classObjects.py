class Parrot:

    # class object attribute
    name = ""
    age = 0

# create Parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create Parrot2 object
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access the class attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
print(parrot1.__dict__)