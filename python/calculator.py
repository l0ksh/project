#!/bin/usr/python3

#This is a basic calculator

#Addition
def add(v1,v2):

	res = v1 + v2
	print('Result:',res)

#Subtraction
def subtract(v1,v2):

	res = v1 - v2
	print('Result:', res)

#Multiplication
def multiply(v1,v2):

	res = v1 * v2
	print('Result:', res)

#Division
def divide(v1,v2):

	res = v1 / v2
	print('Result:', res)

#Taking inputs from user
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

print('''Choose the operation to perform: 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
''')

option = int(input('Enter option: '))

match option:
	case 1:
		add(n1,n2)
	case 2:
		subtract(n1,n2)
	case 3:
		multiply(n1,n2)
	case 4:
		divide(n1,n2)
	case 5:
		print('Exiting...')
	case _:
		print("Please chooose correct option")

