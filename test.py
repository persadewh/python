#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

print('Hello')


print('%s is programming.' % ('Python'))

def normalize(name):
    return name.capitalize()

l1 = ['adam','LISA','barT']
l2 = list(map(normalize,l1))
print(l2)
