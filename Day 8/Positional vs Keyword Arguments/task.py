# Functions with input

#def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")

# Functions with more than 1 input
def greet_with(name, age):
    print(f"Olá eu sou o {name}, e tenho {age} anos.")
greet_with("Felipe", 26)

def greet_with(name = "Felipe", age = 26):
    print(f"Olá eu sou o {name}, e tenho {age} anos.")
greet_with()