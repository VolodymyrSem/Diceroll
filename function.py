import random as ran


def dices(typedice):
    if typedice == 6:
        num = ran.randint(1, 6)
        return num
    elif typedice == 8:
        num = ran.randint(1, 8)
        return num
    elif typedice == 12:
        num = ran.randint(1, 12)
        return num
