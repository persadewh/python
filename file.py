
import os

def list_cwd():
    return os.listdir(os.getcwd())


print(list_cwd())

f = open('log.txt','a+')
f.write('Test')

f.close()

'''
'r' 	open for reading (default)
'w' 	open for writing, truncating the file first
'x' 	open for exclusive creation, failing if the file already exists
'a' 	open for writing, appending to the end of the file if it exists
'b' 	binary mode
't' 	text mode (default)
'+' 	open a disk file for updating (reading and writing)
'U' 	universal newlines mode (deprecated)
'''
