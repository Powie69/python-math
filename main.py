from time import sleep
from random import randint, seed, shuffle, choice
from colorama import Fore, Style
import colorama

colorama.init()

Min = 1
Max = 9

isNumSet = False
numSet = [0]

def setNum(Args):
	global isNumSet, numSet
	if len(Args) <= 1:
		isNumSet = False
		return print("setNum disabled")
	for arg in Args[1:]:
		if not arg.isdigit():
			return print(f"'{arg}' is not a number")

	isNumSet = True
	numSet = [int(arg) for arg in Args[1:]]
	print(f"Turning on setNum: {numSet}")

def setRange(Args):
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
	digits = [choice(numSet), randint(Min, Max)] if isNumSet else [randint(Min, Max), randint(Min, Max)]
	shuffle(digits)
	print(f"{digits[0]} + {digits[1]}")
	return sum(digits)

def toggleSeed(Args):
	if len(Args) <= 1:
		print('setting random seed')
		seed(randint(9,32767))
		return
	if not Args[1].isdigit():
		return print('not a number!')
	seed(Args[1])
	print(f'seed toggled to {Args[1]}')


showControls()

while True:
	print(f"{Fore.GREEN}{Style.BRIGHT}Halo~")
	Ans = makeAnser()
	Input = input().lower().split()
	if len(Input) < 1:
		continue
	command = Input[0]
	# print(Input)
	if command == "range":
		setRange(Input)
	elif command == "ts":
		toggleSeed(Input)
	elif command == "sn":
		setNum(Input)
	elif command == str(Ans):
		print(f"{Fore.BLUE}Nice!")
	else:
		print(f"{Fore.RED}wrong mf")
		print(f"Right: {Ans}")
	sleep(.3)