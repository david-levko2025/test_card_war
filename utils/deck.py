import random


def create_card(rank:str,suite:str) -> dict:
    key_card = {}
    key_card["rank"] = rank
    key_card["suite"] = suite
    if rank.isdigit():
        key_card["value"] = int(rank)
    else:
        if rank == "J":
            key_card["value"] = 11
        elif rank == "Q":
            key_card["value"] = 12
        elif rank == "K":
            key_card["value"] = 13
        elif rank == "A":
            key_card["value"] = 14

    return key_card



def  compare_cards(p1_card:dict, p2_card:dict) -> str:
    value_p1 = p1_card["value"]
    value_p2 = p2_card["value"]
    if value_p1 > value_p2:
        return "p1"
    elif value_p2 > value_p1:
        return "p2"
    else:
        return "WAR"



def create_deck() -> list[dict]:
    all_deck = []
    deck = {}
    all_markings = ["H","C","D","S"]
    after_ten = ["J","Q","K","A"]
    for i in range(2,15):
        for j in range(4):

            if i <= 10:
                deck["rank"] = str(i)
                deck["suite"] = all_markings[j]
                deck["value"] = i
            else:
                deck["rank"] = after_ten[i-12]
                deck["suite"] = all_markings[j]
                deck["value"] = i
            all_deck.append(deck)
            deck = {}
    return all_deck




def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):
        index1 = random.randint(0,51)
        index2 = random.randint(0,51)
        if index1 != index2:
            deck[index1] , deck[index2] = deck[index2] ,deck[index1]

    return deck


