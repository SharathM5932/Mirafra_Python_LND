import socket
s=socket.socket()
s.bind(('localhost',9999))
s.listen(3)
while True:
    con,address=s.accept()
    name=con.recv(1024).decode()
    print("connected to:",address,con,name)
    con.send(bytes('connected to server','utf-8'))
    con.close()
