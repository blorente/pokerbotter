from player import *
from pokerFlow.pokerFlow import Game

players = []
board = [{"NULL": "NULL"} for i in range(0,5)]

def main():
    game = Game()
    players.append(MinraisePlayer("Player1", 500))
    players.append(CallPlayer("Player2", 500))
    game.playHand(players, 0)


main()
