import os
from replit import clear
from blind_auction_art import logo

print(logo)
def add_persons(name, bid):
    people = {
        'name': name,
        'bid': bid
    }
    list_of_bids.append(people)
    print(list_of_bids)

ask = True
list_of_bids = []

while ask == True:
    name = input('What is our name?: ')
    bid = int(input("What's your bid?: $"))
    add_persons(name, bid)
    answer = input('Are there any other bidders? type "yes" or "no": ').lower()
    if answer == 'yes':
        os.system('cls')
    else:
        ask = False
        max = {'name':'', 'bid':0}
        for value in list_of_bids:
            if value['bid'] > max['bid']:
                max = value
        print(f"The winner is {max['name']} with a bid of ${max['bid']}")
