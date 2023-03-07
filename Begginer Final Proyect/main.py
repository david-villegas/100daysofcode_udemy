'''
1) Importar Random (para listas)
2) Importar os
3) Contador que sume los puntos acumulados
4) En la Var A se debe guardar y sustituir la anterior si la repuesta es correctas
5) Opción B debe ser una selección random
6) Si la respuesta es incorrecta (la opción elegida es menor que la otra), termina  el juego.
'''
from art import logo, vs
from game_data import data
import random
from replit import clear

def import_data():
    return random.choice(data)


def game():
    clear()
    print(logo)
    points = 0
    end_game = False
    a_option = import_data()
    b_option = import_data()

    while not end_game:
        print(f"Compare A: {a_option['name']}, a {a_option['description']}, from {a_option['country']}")
        print(vs)
        print(f"Compare B: {b_option['name']}, a {b_option['description']}, from {b_option['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess.lower() == 'a':
            if a_option['follower_count'] > b_option['follower_count']:
                points += 1
                print(f"You're right! Current score: {points}")
                b_option = import_data()
            else:
                clear()
                print(logo)
                print(f"Sorry, that's wrong. Final score: {points}")
                end_game = True
        else:
            if b_option['follower_count'] > a_option['follower_count']:
                points += 1
                print(f"You're right! Current score: {points}")
                a_option = b_option
                b_option = import_data()
            else:
                clear()
                print(logo)
                print(f"Sorry, that's wrong. Final score: {points}")
                end_game = True


game()
