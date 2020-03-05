"""
File: wheel.py
Module for playing roulette with Classes Pocket and Wheel
"""
import random


class Pocket(object):
    """A wheel object with Number, Paired, and Color"""
    RANKS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36)
    PAIRED = ('Odd', 'Even', 'Zero')
    COLOR = ('Red', 'Black', 'Green')

    def __init__(self, rank, paired, color):
        """Creates a wheel number with the given rank, paired and color"""
        self.rank = rank
        self.paired = paired
        self.color = color


def determine_pair(number):
    print(number)
    if (num % 2) == 0:
        pair = 'even'
    elif number == 1 or 3 or 5 or 7 or 9 or 11 or 13 or 15 or 17 or 19 or 21 or 23 or 25 or 27 or 29 or 31 or 33 or 35:
        pair = 'odd'
    elif number == 0:
        pair = "zero"
    else:
        pair = 'undetermined'
    print(pair)
    return pair


def determine_color(number):
    print(number, "  print in determine color")
    redlist = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    blacklist = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    if number in redlist:
        color = "red"
    elif number in blacklist:
        color = "black"
    elif number == 0:
        color = 'green'
    else:
        color = "undetermined"
    print(color, "color in wheel line 49")
    return color


class Wheel(object):
    """ A Wheel containing 36 numbers"""

    def __init__(self):
        """Creates Attribution to pocket landing"""
        self._pockets = list(range(0, 36))

    def spin(self):
        """equivalent of spinning the wheel"""
        random.shuffle(self._pockets)

    def landed_number(self):
        """Removes the top number from array as a result of spinning the wheel"""
        if len(self) == 0:
            return None
        else:
            return self._pockets[14]

    def __len__(self):
        """Returns the number of spins left in the queue"""
        return len(self._pockets)

    def __str__(self):
        result = ''
        for p in self._pockets:
            result = self.result + str(p) + '\n'
        return result
        """Returns the string representation of the pockets"""

