from string import ascii_uppercase
import random
class Robot(object):
    def __init__(self):
        self.name = self.generate_name()


    def reset(self):
        self.name = self.generate_name()

    def generate_name(self):
        random.seed()
        uppercaseLetterSelection = random.choices(ascii_uppercase,k=2)
        generated_name = f'{uppercaseLetterSelection[0]}{uppercaseLetterSelection[1]}'
        stringLength=len(generated_name)
        while stringLength < 5:
            generated_name += str(random.randrange(10))
            stringLength = len(generated_name)
        return generated_name
