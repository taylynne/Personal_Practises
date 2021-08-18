class Playing_card:

    def __init__(self, card_num, card_suit):
        self.rank = card_num
        self.suit = card_suit

    @property
    def color(self):
        if self.suit.lower() == "hearts" or self.suit.lower() == "diamonds":
            return "red"
        else:
            return "black"


card_1 = Playing_card(1, "spades")

print(card_1.color)