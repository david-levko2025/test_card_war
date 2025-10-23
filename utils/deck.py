def create_card(rank:str,suite:str) -> dict:
    full_deck =[]
    rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suite = ['H','C','D','S']
    for rank in range(len(rank)):
        for suite in range(len()):
            full_deck.append(rank)
create_card('A','S')

def compare_cards(p1_card:dict,p2_card:dict) -> str:
    p1_card = create_card()
    p2_card = create_card()

    if p1_card == p2_card:
        print('WAR')
    elif p1_card > p2_card:
        print('p1')
    else:
        print('p2')
    return compare_cards
compare_cards()

def create_deck() -> list[dict]:
    rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suite = ['H', 'C', 'D', 'S']
    for rank in list(suite):
        print(len(create_deck()))
create_deck()

def shuffle(deck:list[dict])-> list[dict]:
    import random

    index_1 = create_deck()
    index_2 = create_deck()
    first_contestant = index_1
    second_contestant = index_2
    for a in range(1000):
        shuffles = random.randint(1,52)




