import socket

server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_Socket.bind(('localhost', 15000))
server_Socket.listen(5) 

while True:
    print("Server menunggu koneksi..")
    client_Socket,addr = server_Socket.accept() 
    print("koneksi klien dari ",addr)
    while True:
        data = client_Socket.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        print("pesan client : ",data.decode("utf-8"))
        try:
            client_Socket.send(bytes('heh client','utf-8'))
        except:
            print("Keluar")
    client_Socket.close()
server_Socket.close()
