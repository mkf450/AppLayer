from socket import *
import base64

msg = "\r\n I love Computer Networks"
endmsg = "\r\n.\r\n"

# Fill in start
mailserver = ("mail.smtp2go.com", 2525)  
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
print(b"Message after connection request:" + recv)
if recv[:3] != b'250':
    print('250 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1.decode())
if recv1[:3] != b'250':
    print('250 reply not received from server.')

# Info for username and password
username = "mkeenanf@students.undip.ac.id"  # the username for your server
password = "uoVqaMQXyX78"  # the password for your server, changed here
base64_str = ("\x00" + username + "\x00" + password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())
if recv_auth[:3] != b'235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <mkeenanf@students.undip.ac.id> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
print(b"After MAIL FROM command: " + recv2)
if recv2[:3] != b'250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <mkeenanf@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
print(b"After RCPT TO command: " + recv3)
if recv3[:3] != b'250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
print(b"After DATA command: " + recv4)
if recv4[:3] != b'354':
    print('354 reply not received from server.')

# Send message data.
subject = "Subject: SMTP mail client testing \r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:" + recv_msg.decode())
if recv_msg[:3] != b'250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message = clientSocket.recv(1024)
print(message)
clientSocket.close()


#cobahalo123