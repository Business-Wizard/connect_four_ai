class GameBoard():
    def __init__(self, shape: tuple=(6, 7)):
        self.shape = shape

    def __repr__(self):
        return f"GameBoard({self.shape})"