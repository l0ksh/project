#!/usr/bin/python3

#Madlib - is program that generates ransom sentences based on some varaibles that are pre defined.

name = input('Name: ')
hobby = input('Hobby: ')
working_status = input('Working Status: ')

madlib = f"Hello, my name is {name}. I am currently {working_status}. \
My hobby is {hobby}."

print(madlib)
