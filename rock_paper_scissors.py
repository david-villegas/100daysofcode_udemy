# https://replit.com/@appbrewery/rock-paper-scissors-start#main.py
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
#Write your code below this line 👇

select = [rock, paper, scissors]
random_select = random.randint(0,2)
option = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if option < 0 or option > 2:
    print('You have selected an invalid option, try again.')
else:
    print(select[option])
    print('Computer chose:\n')
    print(select[random_select])
    if option == 0 and random_select == 2:
        print('You Win')
    elif random_select == 0 and option == 2:
        print('You Lose')
    elif random_select > option:
        print('You Lose')
    elif option > random_select:
        print('You Win')
    elif option == random_select:
        print("It's a Draw")


# if option == 0:
#     print(rock)
#     print('Computer chose:')
#     print(random_select)
#     if random_select == rock:
#         print("It's a Draw")
#     elif random_select == scissors:
#         print('You Win!')
#     else:
#         print('You Lose!')
# elif option == 1:
#     print(paper)
#     print('Computer chose:')
#     print(random_select)
#     if random_select == paper:
#         print("It's a Draw")
#     elif random_select == rock:
#         print('You Win!')
#     else:
#         print('You Lose!')
# else:
#     print(scissors)
#     print('Computer chose:')
#     print(random_select)
#     if random_select == scissors:
#         print("It's a Draw")
#     elif random_select == paper:
#         print('You Win!')
#     else:
#         print('You Lose!')
