# from the socket module import all
from socket import *

# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
clientSocket = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
host_name = gethostbyname('localhost')
server_address = (host_name, 10000)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
clientSocket.connect((server_address))
try:
    message = str(input("Please enter the message you wish to send "))
    # Send data
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    clientSocket.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
    	# Data is read from the connection with recv()
        # decode() function returns string object
        response = clientSocket.recv(1024).decode()
        amount_received += len(message)
    print('received "%s" from server' % response)

finally:
    print('closing socket')
    clientSocket.close()

