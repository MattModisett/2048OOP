class Cell:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        self.value += other.value
        other.value = 0
