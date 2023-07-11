#!/usr/bin/python3

import random

def guess(v):
	random_number = random.randint(1,v)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {v}: '))
		if guess > random_number:
			print('Guess again. Too high')
		elif guess < random_number:
			print('Guess again. Too low')
			
	print(f'Yay, you guessed it right: {guess}')

def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:	
			guess = random.randint(low, high)
		else:
			guess = low #could also be high b/c low = high
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower()
		if feedback == "h":
			high = guess - 1
		elif feedback == "l":
			low = guess + 1
	
	print(f'Yay, The computer guessed your number, {guess}, correctly!')

computer_guess(100)
#guess(10)
