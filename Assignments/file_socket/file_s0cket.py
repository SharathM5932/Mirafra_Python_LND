#client
import socket
s=socket.socket()
s.connect(('localhost',9999))
#run the server and then the client
#note the server after running the client: connected with address
#59730 is client's port no.
name=input('enter your name')
s.send(bytes(name,'utf-8'))
print(s.recv(1024))