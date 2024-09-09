import art
import random

print(art.logo)
print("I'm thinking og a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard'\n").lower()
secret_number = random.randrange(1,101)

if level == "easy":
    chances = 10
    while chances > 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        if secret_number > answer:
            print("To low")
            chances -= 1
        elif secret_number < answer:
            print("To high")
            chances -= 1
        elif secret_number == answer:
            print(f"You got it! the answer was {secret_number}")
            break

if level == "hard":
    chances = 5
    while chances > 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        if secret_number > answer:
            print("To low")
            chances -= 1
        elif secret_number < answer:
            print("To high")
            chances -= 1
        elif secret_number == answer:
            print(f"You got it! the answer was {secret_number}")
            break