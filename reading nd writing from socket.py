from socket import*
HOST = " "
#%socket.setdefaulttimeout(2)
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168", 21))
ans = s.recv(1024)
print(ans)

