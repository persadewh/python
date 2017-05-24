import socket

socket.setdefaulttimeout(5)

s = socket.socket()
# i = 65535
# while i > 0:
#     try:
#         s.connect(("localhost", i))
#         i = i-1
#         ans = s.recv(1024)
#         print(ans)
#     except ConnectionRefusedError:
#         print('error')

port = 80
s.connect(("www.baidu.com", port))
msg = s.recv(1024)
print(msg)

