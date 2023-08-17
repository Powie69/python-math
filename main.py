from time import sleep
from random import randint, seed
from colorama import Fore, Style
import colorama

colorama.init()

Min = 1
Max = 9

Seed = 69420
seedToggled = False

def setRange(min=1,max=9):
    Min = min
    Max = max
    print("")

def showControls():
    print("Controls:")
    print('"S" = start')
    print('"range" = set the range of numbers')
    print('"ts" = toggle seeding')
    print('"ss" = set seed')
    # print('"S" = start')

def makeAnser():
    first = randint(Min,Max)
    second = randint(Min,Max)
    print(f"{first} + {second}")
    return first + second

def toggleSeed():
    global seedToggled
    if seedToggled == True:
        seed(randint(9,32767))
        print("turning off seed")
    else:
        seed(Seed)
        seedToggled = True
        print("turning on seed")

def setSeed():
    Input = input("enter seed: ")
    Seed = Input

while True:
    print(f"{Fore.GREEN}{Style.BRIGHT}Halo~")
    showControls()
    Input = input().lower()
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
    elif Input == "ts":
        toggleSeed()
    elif Input == "ss":
        setSeed()        

    
    
    sleep(1)