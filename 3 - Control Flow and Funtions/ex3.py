import random
import sys


def chooseRandom():
    try:
        userChoose = int(input("Choose number from 1 to 15: "))
        num = round(random.random()*15)

        if 0 < userChoose and userChoose < 16:
            if userChoose == num:
                return print("You win!")
            else:
                return print("You lose")
        else:
            return print("You can't choose {}".format(userChoose))

    except ValueError:
        print()
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.Need number.")
        print()
        chooseRandom()


chooseRandom()
