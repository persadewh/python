#!/usr/local/bin/python3

'''
comments
'''

"""
comments
"""

# comment


a = b = c = 1
a, b, c = 1, 2, "ray"

print(c)

#Number
var1 = 10
del var1

'''
int
long
float
complex
'''




#String
str = "Hello World "
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "Test ")

#List
list = ['1','2','3','4']
raylist = [123,'ray']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(raylist * 2)
print(list + raylist)

list[3] = '55555'
print(list)

#Tuple
#the data in tuple can't be modified
tuple = ('a','b','c')
print(tuple)

#Sets
#无序不重复的序列
student = {'1','2','3','4','4'}
print(student)
print('1' in student)

#Dictionary
#key:value
raydict = {1:'1',2:'2','3':3}
print(raydict)
print(raydict[2])
print(raydict.keys())

