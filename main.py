from time import sleep
from random import randint, seed
from colorama import Fore, Style
import colorama

colorama.init()

Min = 1
Max = 9


def setRange(min=1,max=9):
    Min = min
    Max = max
    print("")

def showControls():
    print("Controls:")
    print('"S" = start')
    print('"range" = set the range of numbers')
    # print('"S" = start')

def makeAnser():
    first = randint(Min,Max)
    second = randint(Min,Max)
    print(f"{first} + {second}")
    return first + second

while True:
    print(f"{Fore.GREEN}{Style.BRIGHT}Halo~")
    showControls()
    Input = input()
    if Input == "s":
        while True:
            Ans = makeAnser()
            Input = input().lower()
            if Input == "c":
                break
            elif Input == str(Ans):
                print(f"{Fore.BLUE}Nice!")
            else:
                print(f"{Fore.RED}wrong mf")
                print(f"Right: {Ans}")
            sleep(.3)

    
    
    sleep(1)