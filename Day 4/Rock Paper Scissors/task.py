import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Person choose
human_number_choose = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if human_number_choose == 0:
    print(rock)
    print("Rock")
elif human_number_choose == 1:
    print(paper)
    print("Paper")
elif human_number_choose == 2:
    print(scissors)
    print("Scissors")

# Computer choose
computer_number_choose = random.randint(0,2)
if computer_number_choose == 0:
    print(rock)
    print("Rock")
elif computer_number_choose == 1:
    print(paper)
    print("Paper")
elif computer_number_choose == 2:
    print(scissors)
    print("Scissors")

#Game
if human_number_choose == computer_number_choose:
    print("Draw")
elif human_number_choose == 0 and computer_number_choose == 1:
    print("You Lose!")
elif human_number_choose == 0 and computer_number_choose == 2:
    print("You Win!")
elif human_number_choose == 1 and computer_number_choose == 0:
    print("You Win!")
elif human_number_choose == 1 and computer_number_choose == 2:
    print("You Lose!")
elif human_number_choose == 2 and computer_number_choose == 0:
    print("You Lose!")
elif human_number_choose == 2 and computer_number_choose == 1:
    print("You Win!")