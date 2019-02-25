# Score categories
# Change the values as you see fit
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: single_dice_num(x,1)
TWOS = lambda x: single_dice_num(x,2)
THREES = lambda x: single_dice_num(x,3)
FOURS = lambda x: single_dice_num(x,4)
FIVES = lambda x: single_dice_num(x,5)
SIXES = lambda x: single_dice_num(x,6)
FULL_HOUSE = lambda x: sum(x) if len(set(x)) == 2 and x.count(x[0]) in [2,3] else 0
FOUR_OF_A_KIND = lambda x: sum(4 * y for y in set(x) if x.count(y) >= 4)
LITTLE_STRAIGHT = lambda x: 30 * (sorted(x) == [1,2,3,4,5])
BIG_STRAIGHT = lambda x: 30 * (sorted(x) == [2,3,4,5,6])
CHOICE = lambda x: sum(x)

def single_dice_num(x, num):
    return num * x.count(num)

def score(dice, category):
    return category(dice)
