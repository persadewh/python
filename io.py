#

# name = input('Input you name : ').strip()

# print(name.capitalize())


#define function
def myf(name):
    #return
    return 'this is ' + name


print(myf('ray'))

myname = 'ray'

def say():
    print('hello ' + myname)

def change(name):
    myname = name

def changeglobal(name):
    global myname
    myname = name

say()

change('martin')

say()

changeglobal('martin')

say()

name = input()
print(name)


if name == 'weihao':
    print('yes')
else:
    print('no')

def myabs(x):
    if x >= 0:
        return x;
    else:
        return -x;







