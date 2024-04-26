# import random

# random_int = random.randint(1,10)
# print(random_int)

# random_float = random.random() * 5
# print(random_float)

# Index out of range error : 

# Index starts from 0 to len-1 if we are tring to access 
# Something out of this range we get ERROR - INDEX_OUT_OF_RANGE

# list in list : list = [list1 , list2]

# Random and Lists

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

import random

game_images = [rock,paper,scissors]

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!")
else:

    print(game_images[choice])
    computer_choice = random.randint(0,2)
    print('Computer Chose:')
    print(game_images[computer_choice])

    # decision

    
    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and choice == 2:
        print("You lose")
    elif computer_choice > choice:
        print("You lose")
    elif choice > computer_choice:
        print("You win!")
    elif computer_choice == choice:
        print("It's a draw")
