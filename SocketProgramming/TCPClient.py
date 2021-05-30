import socket

client_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_Socket.connect(('localhost',15000))
payload = 'Loreum Ipsum jirolu'
try:
    while True:
        client_Socket.send(payload.encode('utf-8'))
        data = client_Socket.recv(1024)
        print(str(data))
        more = input('Lagi? (y/n) ')
        if more.lower() == 'y':
            payload = input('Masukkan data : ')
        else:
            break
except KeyboardInterrupt:
    print("Keluar")
client_Socket.close()
