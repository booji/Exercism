import string
# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def is_ongoing(func):
        def wrapper(self, *args):
            if self.status != STATUS_ONGOING:
                raise ValueError(
                    f"End game state already reached: {self.status}")
            return func(self, *args)
        return wrapper

    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.__word = word.lower()
        self.char_guess = set()

    @is_ongoing
    def guess(self, char):
        char = char.lower()
        if char in self.char_guess:
            self.remaining_guesses -= 1
        elif char in self.__word:
            self.char_guess.add(char)
        else:
            self.remaining_guesses -= 1
        self.get_status()

    def get_masked_word(self):
        table = str.maketrans(
            {key: key if key in self.char_guess else '_'
             for key in string.ascii_letters})
        return self.__word.translate(table)

    def get_status(self):
        if self.status in [STATUS_WIN, STATUS_LOSE]:
            return self.status
        if set(self.__word) == self.char_guess:
            self.status = STATUS_WIN
            self.remaining_guesses = 0

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        return self.status
