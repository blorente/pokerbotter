from deck import Deck

players = []
board = [{"NULL": "NULL"} for i in range(0,5)]

def main():
    deck = Deck()
    print(deck.cards)
    dealt = deck.deal(4)
    print(dealt)
    print(deck.cards)


def playHand(players, button):
    print(str(board))

main()
