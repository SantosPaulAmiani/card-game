import random
suits = ('Hearts','Diamond','Spades','Flowers')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = [rank]

    def __str__(self):
        return self.rank + " of " + self.suit


new_card = Card('Hearts', 'Two')
print(new_card)


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()
first_card = new_deck.all_cards[20]
print(first_card)
print(len(new_deck.all_cards))


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_card):
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)


    def __str__(self):
        return f'Player{self.name} has {len(self.all_cards)} cards.'


new_player = Player(" Jose")
new_player.add_cards(mycard)
new_player.add_cards([mycard, mycard, mycard])
print(new_player.all_cards[0])
new_player.remove_one()
print(new_player)

player_0ne = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_0ne.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


print(len((player_0ne.all_cards)))
game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')
    if len(player_0ne.all_cards) == 0:
        print("player one, out of cards! player two wins")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("player two, out of cards! player one wins")
        game_on = False
        break

    player_0ne_cards = []
    player_0ne_cards.append(player_0ne.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_0ne_cards[-1].values > player_two_cards[-1].values:
            player_0ne.add_cards(player_0ne_cards)
            player_0ne.add_cards(player_two_cards)
            at_war = False
        elif player_0ne_cards[-1].values < player_two_cards[-1].values:
            player_two.add_cards(player_0ne_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR')
            if len(player_0ne.all_cards) < 3:
                print("Player one unable to declare war")
                print('Player two wins')
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player two unable to declare war")
                print('Player one wins')
                game_on = False
                break
            else:
                for num in range(3):
                    player_0ne_cards.append(player_0ne.remove_one())
                    player_two_cards.append(player_two.remove_one())
