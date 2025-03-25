import  socket
s=socket.socket()
s.connect(('localhost',9999))
name=input("enter:")
s.send(bytes(name,'utf-8'))
print(s.recv(1024))
while True:


