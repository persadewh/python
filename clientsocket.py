#!/usr/local/bin/python3
import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('rayweihao',9999))

msg = s.recv(1024)

s.close()

print(msg)