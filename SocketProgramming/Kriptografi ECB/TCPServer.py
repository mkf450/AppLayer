import socket

# Inisialisasi pemuatan soket dan memulai mendengarkan  TCP request yang akan datang
server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# mengset soket ke alamat lokal, Isiannya sepasang yaitu (host,port). host harus diisi alamat lokal yaitu localhost atau 127.0.0.1
server_Socket.bind(('localhost', 15000))

# mengaktifkan server untuk menerima koneksi. Argumen backlog harus di isi minimal angka 0 (jika lebih rendah, akan diset ke 0);
server_Socket.listen(5)

while True:
    print("Server menunggu koneksi")
    # Terima koneksi. Soket harus di-bind ke sebuah alamat dan listening koneksi. Return value nya adalah sepasang (conn, address) di mana conn adalah objek soket baru yang dapat digunakan untuk mengirim dan menerima data pada sambungan, dan address adalah alamat yang terikat ke soket di ujung sambungan lainnya.
    client_Socket, addr = server_Socket.accept()
    print("Koneksi klien dari: ", addr)
    while True:
        data = client_Socket.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        print("Menerima dari client: ", data.decode("utf-8"))
        try:
            client_Socket.send(bytes('Halo Client', 'utf-8'))
        except:
            print("Keluar")
    client_Socket.close()
server_Socket.close()
