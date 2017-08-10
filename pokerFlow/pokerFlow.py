from pokerFlow.deck import Deck


class Game():
    def __init__(self):
        self.deck = Deck()
        self.pot = 0
        self.board = []

    def setupHand(self, players):
        self.deck.shuffle()
        self.pot = 0
        self.board = []
        for p in players:
            p.curBet = 0
            p.isInHand = True
            p.holeCards = self.deck.deal(2)

    def playHand(self, players, buttonIndex):
        # Preflop
        self.setupHand(players)
        print("Stacks:")
        for player in players:
            print("%s (%d) is on the %s" % (
            player.name, player.chips, ("SB" if player.name == players[buttonIndex].name else "BB")))
        print(players[buttonIndex].name + " is in the Button.")
        self.getAction(buttonIndex, players)

        # Flop
        self.collectBets()
        self.dealFlop()
        self.getAction(buttonIndex + 1, players)

        # Turn
        self.collectBets()
        self.dealTurn()
        self.getAction(buttonIndex + 1, players)

        # River
        self.collectBets()
        self.dealRiver()
        self.getAction(buttonIndex + 1, players)


    def interpretAction(self, player, command, lastBet):
        commandParts = command.split(' ')
        action = commandParts[0]
        amount = int(commandParts[1])
        if action == "raise":
            player.chips = player.chips - ((lastBet + amount) - player.curBet)
            player.curBet = lastBet + amount
            return lastBet + amount
        elif action == "check":
            return 0
        elif action == "call":
            player.chips -= lastBet
        elif action == "fold":
            player.isInHand = False

    def showdown(self):
        pass

    def dealFlop(self):
        pass

    def dealTurn(self):
        pass

    def dealRiver(self):
        pass

    def getAction(self, firstSpeaker, players):
        bet = 0
        for i in range(firstSpeaker, firstSpeaker + len(players)):
            player = players[i % len(players)]
            print("Action on %s. Pot is %d " % (player.name, self.pot))
            if (player.chips > 0 && player.isInHand):
                action = player.action(self.board, self.pot, bet)
                print("%s: %s" % (player.name, action))
                bet = self.interpretAction(player, action)

    def collectBets(self, players):
        for p in players:
            self.pot += p.curBet
            p.curBet = 0


