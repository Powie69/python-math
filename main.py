from time import sleep
from random import randint, seed, shuffle
from colorama import Fore, Style
import colorama

colorama.init()

Min = 1
Max = 9

seedToggled = False
isNumSet = False
numSet = None

def setNum(Args):
	global isNumSet, numSet
	if len(Args) <= 1:
		isNumSet = False
		return print("setNum disabled")
	if not Args[1].isdigit():
		return print('not a number')
	isNumSet = True
	numSet = int(Args[1])
	print(f"Turning on setNum: {numSet}")

def	setRange(Args):
	if len(Args) < 3:
		return
	global Min, Max
	try:
		Min = int(Args[1])
		Max = int(Args[2])
	except ValueError:
		print(f'{Fore.RED}Arguments must be Integers{Fore.RESET}')
	print(f"Min: {Args[1]}, Max: {Args[2]}")

def showControls():
	print("Controls:")
	print('"S" = start')
	print('"range" = set the range of numbers')
	print('"ts" = toggle seeding')
	print('"sn" = set number')

def makeAnser():
	digits = [numSet, randint(Min, Max)] if isNumSet else [randint(Min, Max), randint(Min, Max)]
	shuffle(digits)
	print(f"{digits[0]} + {digits[1]}")
	return sum(digits)

def toggleSeed(Args):
	global seedToggled
	if len(Args) <= 1:
		print('setting random seed')
		seed(randint(9,32767))
		return
	if not Args[1].isdigit():
		return print('not a number!')
	seed(Args[1])
	print('')


showControls()

while True:
	print(f"{Fore.GREEN}{Style.BRIGHT}Halo~")
	Input = input().lower().split()
	command = Input[0]
	print(Input)
	if command == "s":
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
	elif command == "range":
		setRange(Input)
	elif command == "ts":
		toggleSeed(Input)
	elif command == "sn":
		setNum(Input)
	else:
		print("what u talkin' about?")
	sleep(.5)