class Allergies(object):
    allergie_list = ['eggs',
                    'peanuts',
                    'shellfish',
                    'strawberries',
                    'tomatoes',
                    'chocolate',
                    'pollen',
                    'cats']

    def __init__(self, score):
        self.allergy=[(score>>i) & 1 for i,x in enumerate(self.allergie_list)]

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        lst = [a for a, t in zip(self.allergie_list,self.allergy) if t]
        return lst
