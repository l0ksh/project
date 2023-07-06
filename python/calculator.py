#!/bin/usr/python3

#This is a basic calculator


#Taking inputs from user
var1 = input('Enter first number: ')
var2 = input('Enter second number: ')

#Addition
def add(v1,v2):

	res = int(v1) + int(v2)
	print('The sum is:',res)

#Subtraction
def subtract(v1,v2):

	res = int(v1) - int(v2)
	print('The subtraction is:', res)

#Multiplication
def multiply(v1,v2):

	res = int(v1) * int(v2)
	print('The multiplication is:', res)

#Division
def divide(v1,v2):

	res = int(v1) / int(v2)
	print('The division is:', res)

add(var1,var2)
