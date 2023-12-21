#rock-paper-scissor game (semi-graphical)

import random

print("Welcome to the game!\nCreated on 16-11-2021")
rock = '''
    ________
---'   _____)
      (______)
      (______)
      (_____)
---.__(____)
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

Game = 'Y'

while Game == 'Y':

    human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if human_choice == 0:
        print(f"You Choosed:ROCK\n {rock}")
    elif human_choice == 1:
        print(f"You Choosed:PAPER\n {paper}")
    elif human_choice == 2:
        print(f"You Choosed:SCISSOR\n {scissors}")


    print("/////////////////////////////////////////////////////////////////////")

    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(f"Computer Choosed:ROCK\n {rock}")
    elif computer_choice == 1:
        print(f"Computer Choosed:PAPER\n {paper}")
    elif computer_choice == 2:
        print(f"Computer Choosed:SCISSOR\n {scissors}")

    
    if computer_choice == human_choice:
        print("It's an draw")
    elif computer_choice == 0 and human_choice == 1:
        print("You won")
    elif computer_choice == 0 and human_choice == 2:
        print("You lose")
    elif computer_choice == 1 and human_choice == 0:
        print("You lose")
    elif computer_choice == 1 and human_choice == 2:
        print("You won")
    elif computer_choice == 2 and human_choice == 0:
        print("You won")
    elif computer_choice == 2 and human_choice == 1:
        print("You lose")
    elif human_choice >= 3:
        print("You typed an invalid number, You LOSE!")
    Game = input("Want to play again (Y/N)?")

rate = int(input("Please rate me on the scale of 5? "))

if rate <= 3:
    print("You are noob!")
elif rate == 4:
    print("Thanks for 4, Help me to improve")
elif rate == 5:
    print("Go and Sleep!")
else:
    print(f"Thanks for giving me more than I deserve- {rate} on the scale of 5")
