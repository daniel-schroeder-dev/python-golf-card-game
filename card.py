from rank import Rank


class Card:
    _rank_to_value = {
        Rank.KING: 0,
        Rank.ONE: 1,
        Rank.TWO: 2,
        Rank.THREE: 3,
        Rank.FOUR: 4,
        Rank.FIVE: 5,
        Rank.SIX: 6,
        Rank.SEVEN: 7,
        Rank.EIGHT: 8,
        Rank.NINE: 9,
        Rank.TEN: 10,
        Rank.JACK: 10,
        Rank.QUEEN: 10,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        return Card._rank_to_value[self.rank]

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"

    def __repr__(self):
        return f"Card({self.rank.name}, {self.suit.name})"

    def __gt__(self, other):
        return self.value > other.value
