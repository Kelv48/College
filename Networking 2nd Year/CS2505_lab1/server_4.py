# from the socket module import all
"""<INSERT CODE TO IMPORT SOCKET MODULE>"""
from socket import *
from datetime import *

# Create a TCP server socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
"""<INSERT CALL TO CREATE THE SOCKET>"""
serverSocket = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# server_localhost = ("localhost", 10000)
hostname = "localhost"
ip_address = gethostbyname('server address ipv4 address on host pc')
portNumber = 10000
bufferSize = 16

# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ' % ('', portNumber))

# Bind the socket to the host and port
"""<INSERT CODE TO BIND SERVER ADDRESS TO SOCKET>"""
serverSocket.bind(('', portNumber)) 

# Listen for one incoming connections to the server
"""<INSERT CODE TO TELL SERVER TO LISTEN FOR ONE INCOMING CONNECTION>"""
serverSocket.listen(1) # 1 for true

# we want the server to run all the time, so set up a forever true while loop
while True:
    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = serverSocket.accept() # <INSERT CODE TO ACCEPT THE CONNECTION REQUEST FROM THE CLIENT>
    
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(bufferSize).decode()
            try:
                if data is not int: 
                    data = int(data)
                    # dataList = data.split("*")
                    bufferSize = data
                    statusMsg = "ready"
                    connection.sendall(statusMsg.encode())
            except:
                pass

            if data:
                data = connection.recv(bufferSize).decode()
                print('received "%s"' % data)
                currentTime = datetime.now()   # timestamp 
                timeStamp = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
                loggedData = f'{timeStamp}: {data}\n'

                # Check if the log file exists, create one if it doesn't
                logFilePath = 'log.txt'
                with open(logFilePath, 'a') as logDataFile:
                    logDataFile.write(loggedData)

                # Send acknowledgment with timestamp back to the client
                response = f"Server logged: '{data}' at {timeStamp}."
                bufferLength = len(response.encode())   # find the size of buffer required for the return message
                bufferLength = str(bufferLength)
            
                connection.sendall(bufferLength.encode())

                checkData = connection.recv(bufferSize).decode()
                if checkData == "ready": 
                    # encode() function returns bytes object
                    connection.sendall(response.encode())
                    print('Sent acknowledgment to client: "%s"' % response)
                else:
                    pass
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        """<INSERT CODE TO CLOSE THE CONNECTION>"""
        connection.close()
        bufferSize = 16

# now close the socket  
serverSocket.close()

