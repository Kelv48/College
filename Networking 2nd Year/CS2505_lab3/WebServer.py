from socket import *

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789
hostname = gethostname()
ip_address = gethostbyname(hostname)
print(hostname, ip_address)

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
    print('Ready to serve...')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode()
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        # Split the message by spaces and take the second part
        filename = message.split()[1]

        # Check if the filename ends with '/' (indicating a directory)
        if filename.endswith('/'):
            # If it's a directory, append 'index.html' to the filename
            filename += 'index.html'

        # Open the requested file
        with open(filename[1:], 'r') as f:
            # Store the entire content of the requested file in a temporary buffer
            outputdata = f.read()

        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the connection socket
        connectionSocket.sendall(outputdata.encode())

        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Close the client connection socket
        connectionSocket.close()

# Close the server socket
serverSocket.close()

