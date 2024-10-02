from socket import *
import time
import threading

server = socket(AF_INET, SOCK_STREAM)

hostname = gethostname()
ip_address = gethostbyname(hostname)
print(hostname, ip_address)
port = int(input("Enter port number you want to listen from: "))
server_address = (hostname, port)
print('*** Server is starting up on %s port %s ***' % server_address)

server.bind(server_address)
server.listen()

def sending():
    while True:
        # Send data
        message = input()
        # Data is transmitted to the server with sendall()
        # encode() function returns bytes object
        connection.sendall(message.encode())

def receiving():
    while True:
        data = connection.recv(1024).decode()
        while not data:
            data = connection.recv(1024).decode()

        print("Client:", data)

while True:
    print('*** Waiting for a connection ***')
    connection, client_address = server.accept()
    
    try:
        print('connection from', client_address)
        print("Message Started")
        current_time = None

        
        thread1 = threading.Thread(target=receiving)
        thread1.start()

        while True:
            # Send data
            message = input()
            # Data is transmitted to the server with sendall()
            # encode() function returns bytes object
            connection.sendall(message.encode())


    
    except ConnectionResetError:
        print("Connection closed by client")
        
    finally:
        connection.close()

server.close()
