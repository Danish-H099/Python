import socket
HOST = '10.1.3.133' #Server ip yes its Server's IP address only
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST ,PORT))
    s.listen()
    conn,addr=s.accept()
with conn:
    while True:
        a=(b'Hey Danish! Got Your Message')
        data=conn.recv(1024)
        print(data)
        if not data:
            break
        conn.sendall(a)