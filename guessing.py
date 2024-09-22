import random


class Guessing:
    def __init__(self, value1):
        self.value1 = value1
    

    def guessed_number(self):
        num = random.randint(1, 100)
        return num