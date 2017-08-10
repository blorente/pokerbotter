class Player:
    def __init__(self, name, startingChips):
        self.name = name
        self.startingChips = startingChips
        self.chips = startingChips
        self.curBet = 0
        self.isInHand = False
        self.holeCards = []

    def action(self, board, pot, bet, BB):
        raise NotImplementedError("Please Implement this method")

    def setCurBet(self, amount):
        self.curBet = amount

class HumanPlayer(Player):
    def action(self, board, pot, bet, BB):
        raw_play = input("Next action: ")
        print(raw_play)

class ShovePlayer(Player):
    def action(self, board, pot, bet, BB):
        return "raise %d" % self.chips

class MinraisePlayer(Player):
    def action(self, board, pot, bet, BB):
        if bet == 0:
            return "bet %d" % BB
        else:
            return "raise %d" % (2 * bet)

class CallPlayer(Player):
    def action(self, board, pot, bet, BB):
        if bet == 0:
            return "check"
        else:
            return "call " % bet
