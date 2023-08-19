from time import sleep
from random import randint, seed
from colorama import Fore, Style
import colorama

colorama.init()

Min = 1
Max = 9

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

def makeAnser():
    first = randint(Min,Max)
    second = randint(Min,Max)
    print(f"{first} + {second}")
    return first + second

def toggleSeed():
    global seedToggled
    if seedToggled == True:
        seed(randint(9,32767))
        seedToggled = False
        print("turning off seed")
    else:
        Input = input("enter seed: ")
        seed(Input)
        print("tfajsdlfjadklfjeiourning on seed")


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
    elif Input == "range":
        minInput = input("enter mininuim: ")
        maxInput = input("enter maxicum: ")
        setRange(minInput,maxInput)
    elif Input == "ts":
        toggleSeed()
   
    
    
    sleep(1)