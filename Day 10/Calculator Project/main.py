import art

# Operações Matemáticas
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))
        answer = operations[operation_symbol](first_number, second_number)
        print(f"The result of {first_number} {operation_symbol} {second_number} is {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()