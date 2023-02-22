sum_cards = [10,10,11]

def calculate_score(sum_cards):
    total_cards = sum(sum_cards)
    if total_cards == 21:
          return 0
    elif total_cards > 21:
        for i in sum_cards:
            if i == 11:
                sum_cards.append(1)
                sum_cards.remove(11)
                print(f'As found and change, {sum_cards}')
        return total_cards
    else:
        return total_cards

calculate_score(sum_cards)
