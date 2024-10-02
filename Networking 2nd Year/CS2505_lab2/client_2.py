# from the socket module import all
from socket import *

# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
sock = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
#hostname = gethostname()
#ip_address = gethostbyname(hostname)
ip_address = input("Enter IP address you want to connect to: ")
port = int(input("Enter port number you want to connect to: "))
server_address = (ip_address, port)

# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
sock.connect(server_address)

try:
    
    while True:
     
        # Send data
        message = input("Client: ")
        # Data is transmitted to the server with sendall()
        # encode() function returns bytes object
        sock.sendall(message.encode())
        
        data = sock.recv(1024).decode()
        while not data:
            data = sock.recv(1024).decode()

        print("Server", data)






finally:
    print('closing socket')
    sock.close()
