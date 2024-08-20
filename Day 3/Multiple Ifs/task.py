print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("The ticket cost $5.")
    elif age <= 18:
        bill= 7
        print("The ticket cost $7.")
    else:
        bill = 12
        print("The ticket cost $12.")

    want_the_photo = input(f"Your bill is {bill}, do you want a photo for $3? Type y for YES and n for NO")
    if want_the_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
