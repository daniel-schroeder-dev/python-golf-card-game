class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"PLAYER: {self.name}"

    def __repr__(self):
        return f"Player({self.name})"
