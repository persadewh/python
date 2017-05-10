#!/usr/local/bin/python3
import socket
import sys

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
print(host)

port = 9999

serversocket.bind((host,port))

serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print(addr)

    clientsocket.send("welcome".encode("utf-8"))
    clientsocket.close()
