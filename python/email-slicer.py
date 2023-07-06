#!/usr/bin/python3

'''
This is an example:

Input: InterviewBit@gmail.com
Output: Your username is InterviewBit & domain is gmail.com

'''

def char_search(string):
	index = string.find('@')
	if index == -1:
		return -1
	else:
		return index

email = input('Enter your email: ')


index = char_search(email)

username = email[0:index]
domain = email[index+1:]

print(f'Your username is {username} & domain is {domain}.')
