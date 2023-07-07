#!/usr/bin/python3

import secrets

#https://www.datacamp.com/tutorial/role-underscore-python

password = ""
for _ in range(12):
  password += secrets.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{[]}\|/,.<>?")

print(password)
