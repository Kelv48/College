# from the socket module import all
from socket import *

# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
clientSocket = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
hostname = "localhost"
ip_address = gethostbyname('server ip ipv4 address on host pc')
portNumber = 10000
bufferSize = 16

# output to terminal some info on the address details
print('connecting to server at %s port %s' %(ip_address, portNumber))

# Connect the socket to the host and port
"""<INSERT CALL TO CONNECT TO SERVER>"""
clientSocket.connect((ip_address, portNumber))  # 2 brackets, first bracket for the param and 2nd for tuple

try:
    # Send data
    message = input("Enter a message from client to server: ")
    print('sending "%s"' % message)

    bufferLength = len(message.encode())
    bufferLength = str(bufferLength)
    clientSocket.sendall(bufferLength.encode())

    statusMsg = clientSocket.recv(bufferSize).decode()
    if statusMsg == "ready":
        # Data is transmitted to the server with sendall()
        # encode() function returns bytes object
        clientSocket.sendall(message.encode())
    else: 
        pass

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
    	# Data is read from the connection with recv()
        # decode() function returns string object
        data = clientSocket.recv(bufferSize).decode()

        try:
            if data is not int: 
                data = int(data)
        except:
            pass

        if type(data) is int :
            bufferSize = data
            booleanMessage = "ready"
            clientSocket.sendall(booleanMessage.encode())
            amount_received += 1    # can be any number
            print('received "%s"' % data)
        else: 
            amount_received += len(data)
            print('received "%s"' % data)

finally:
    print('closing socket')
    clientSocket.close()
    bufferSize = 16
