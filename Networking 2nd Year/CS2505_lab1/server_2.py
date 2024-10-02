# from the socket module import all
from socket import *
from datetime import datetime
from time import strftime

# Create a TCP server socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
serverSocket = socket(AF_INET, SOCK_STREAM)


# set values for host 'localhost' - meaning this machine and port number 10000
host_name = gethostbyname('localhost')
server_address = (host_name, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
serverSocket.bind(("", server_address[1]))
print("The server is ready to receive ")

# Listen for one incoming connections to the server
serverSocket.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = serverSocket.accept()
    
    try:
        print('Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            now = datetime.now()
            log_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            # decode() function returns string object
            data = connection.recv(1024).decode()
            if data:
                print('received "%s" at "%s"' % (data, log_time))
                print('sending data back to the client')
                logFilePath = 'log.txt'
                with open("logFile.txt", "a") as logfile:
                    logfile.write(f"{data}, {log_time}\n")
                    print("Data logged at " + log_time)
                # encode() function returns bytes object
                response_data = f"{data}, {log_time}"
                connection.sendall(response_data.encode())
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()


# now close the socket
serverSocket.close()
