try:
    age = int(input("How old are you?"))
except ValueError:
    print("Type a number")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
