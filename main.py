from time import sleep
from random import randint, seed
from colorama import Fore, Style
import colorama

colorama.init()

Min = 1
Max = 9

seedToggled = False
isNumSet = False
numSet = 0


def setNum():
	global isNumSet
	if isNumSet == True:
		isNumSet = False
		print("Turning off setNum")
	else:
		isNumSet = True
		Input = input("Number: ")
		numSet = Input
		print(f"Turning on setNum: {numSet}")

def	setRange(min=1,max=9):
	Min = min
	Max = max
	print("")

def showControls():
	print("Controls:")
	print('"S" = start')
	print('"range" = set the range of numbers')
	print('"ts" = toggle seeding')

def makeAnser():
	# first = 69
	if isNumSet == True:
		first = numSet
	else:
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
		print("turning on seed")


showControls()

while True:
	print(f"{Fore.GREEN}{Style.BRIGHT}Halo~")
	Input = input().lower()
	if Input == "s":
		# game loop
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
	elif Input == "sn":
		setNum()
	
	else:
		print("what u talkin' about?")
	
	
	sleep(1)