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

guess(10)
