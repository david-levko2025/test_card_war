import 
def create_player(*name :str )-> dict:
    if name:
        player = {"name":str(name[0]),"hand":[],"won_pile":[]}
    else:
        player = {"name":"AI","hand":[],"won_pile":[]}

    return player


def init_game()-> dict:
    p1 = create_player("p1")
    p2 = create_player()
    new_deck = deck.create_deck()
    new_deck = deck.shuffle(new_deck)
    p1["hand"] = new_deck[0:26]
    p2["hand"] = new_deck[26:]
    return {"deck": new_deck,"player_1": p1,"player_2":p2}
def play_round():
    pass