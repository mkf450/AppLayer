import socket

# Data yang akan dikirim
plaintext = '1234E5'

# Kunci didapatkan dari 2 digit terakhir NIM yaitu 52
# 5(10) = 0101(2)
# 2(10) = 0010(2)
# Kunci = 01010010
key = '010100100101001001010010'

# Konversi plaintext ke int lalu ke binary
hex_as_int = int(plaintext, 16)
hex_as_binary = bin(hex_as_int)

# Melakukan operasi XOR terhadap plaintext dengan key
xor_operation = bin(int(hex_as_binary, 2) ^ int(key, 2))

# Melakukan Shift ke kiri
shifting = bin(int(xor_operation, 2) << 1)

# Ciphertext siap dikirimkan
ciphertext = hex(int(shifting[3:], 2))

client_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_Socket.connect(('localhost',15000)) #Hubungkan soket ke remote address. Untuk soket IP, alamatnya adalah sepasang (host, port).
payload = ciphertext #Payload yang dikirim ke server
try:
    while True:
        client_Socket.send(payload.encode('utf-8')) #mengirim data string ke socket
        data = client_Socket.recv(1024) #Menerima hingga 1024 bytes dari socket
        print(str(data))
        more = input('Ingin mengirim data kembali?y/n ')
        if more.lower() == 'y':
            payload = input('Masukkan pesan yang akan dikirim : ')
        else:
            break
except KeyboardInterrupt:
    print("Keluar")
client_Socket.close()
