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

pictures = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid selection, please start the game again")

computer_choice = random.randint(0, 2)

print("Computer chose: ")

print(pictures[computer_choice])

if (user_choice == 0 and computer_choice == 2 or user_choice == 1 and
        computer_choice == 0 or user_choice == 2 and computer_choice == 1):
    print("You Win!")
elif (user_choice == 0 and computer_choice == 1 or user_choice == 1 and
        computer_choice == 2 or user_choice == 2 and computer_choice == 0):
    print("You Lose!")
else:
    print("It's a draw")
