import socket
HOST = '10.1.3.133' # server's ip address
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hey Deepak How are You')
    data=s.recv(1024)

print('Received ',repr(data))

