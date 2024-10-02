from socket import *
import time

server = socket(AF_INET, SOCK_STREAM)

hostname = gethostname()
ip_address = gethostbyname(hostname)
print(hostname, ip_address)
port = int(input("Enter port number you want to listen from: "))
server_address = (hostname, port)
print('*** Server is starting up on %s port %s ***' % server_address)

server.bind(server_address)
server.listen()

while True:
    print('*** Waiting for a connection ***')
    connection, client_address = server.accept()
    
    try:
        print('connection from', client_address)
        current_time = None

        
        while True:
            data = connection.recv(1024).decode()
            if data:
                print("Client", data)
                message = input("Server: ")
                connection.sendall(message.encode())


    
    except ConnectionResetError:
        print("Connection closed by client")
        
    finally:
        connection.close()

server.close()
