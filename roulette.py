"""
File: roulette.py

Module for roulette
Defines Roulette Player and Main Classes
"""


from wheel import Pocket, Wheel, determine_color, determine_pair


class Player(object):
    """This class represents a player in a roulette game"""

    def __init__(self, bet):
        self._bet = bet

    def __str__(self):
        """Returns string of bet"""
        result = map(str, self._bet)
        result += "\n"
        return result


class Roulette(object):

    def __init__(self):
        self._wheel = Wheel()
        self._wheel.spin()

    def play(self):
        print(self._wheel.landed_number(), " line 32")
        print("What would you like to bet on")
        while True:
            games_played = 0
            games_won = 0
            games_played += 1
            choice1 = input("Number/Pair/Color? [n/p/c]: ")
            if choice1 in ("N", "n"):
                choice2 = input("Pick a number [0-36]: ")
                playerbet = choice2
                if playerbet == self._wheel.landed_number():
                    print("You WON!!!!")
                    games_won +=1
                else:
                    print("You lost... Try again")
                break
            elif choice1 in ("P", "p"):
                choice3 = input("Odd or Even? [o/e]: ")
                playerbet = choice3
                if playerbet == determine_pair():
                    print("You WON!!!!")
                    Roulette.games_won += 1
                else:
                    print("You lost... Try again - Line 55")
                break
            elif choice1 in ("C", "c"):
                choice4 = input("Red or Black? [r/b]: ")
                playerbet = choice4
                print(playerbet, "entered answer")
                wheelroll = self._wheel.landed_number()
                print(determine_color(wheelroll), "line 61")
                wheelcolor = 'determine_color(wheelroll)'
                playerbet = 'playerbet.strip()'
                wheelcolor = wheelcolor.strip()
                print(id(playerbet), id(wheelcolor))
                if 'playerbet' == 'wheelcolor':
                    print("You WON!!!!")
                    Roulette.games_won += 1
                else:
                    print("You lost... Try again")
                break
            else:
                print("Issues encountered. Don't know why we are here")
                break
        print(playerbet, "line 71")
        print(self._wheel.landed_number(), "line 72")


def main():
    game = Roulette()
    game.play()


main()
