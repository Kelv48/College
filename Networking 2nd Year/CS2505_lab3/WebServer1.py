from socket import *

def handle_request(client_socket):
    # Receive the request from the client
    request = client_socket.recv(1024).decode()

    # Check if the request starts with 'GET'
    if not request.startswith('GET'):
        # Send '400 Bad Request' response
        client_socket.send("HTTP/1.1 400 Bad Request\r\n\r\n".encode())
        client_socket.send("<html><head></head><body><h1>400 Bad Request</h1></body></html>\r\n".encode())
        client_socket.close()
        return

    # Check if the request contains 'HTTP/1.1'
    if 'HTTP/1.1' not in request:
        # Send '505 HTTP Version Not Supported' response
        client_socket.send("HTTP/1.1 505 HTTP Version Not Supported\r\n\r\n".encode())
        client_socket.send("<html><head></head><body><h1>505 HTTP Version Not Supported</h1></body></html>\r\n".encode())
        client_socket.close()
        return

    # At this point, the request is valid
    # Process the request as before
    filename = request.split()[1][1:]
    try:
        with open(filename, 'rb') as f:
            content = f.read()
        response = "HTTP/1.1 200 OK\r\n\r\n".encode() + content
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode() + "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()

    # Send the response to the client
    client_socket.send(response)
    client_socket.close()

def start_server(server_port):
    # Create a TCP server socket
    server_socket = socket(AF_INET, SOCK_STREAM)
    # Bind the socket to the server address and server port
    server_socket.bind(('', server_port))
    hostname = gethostname()
    ip_address = gethostbyname(hostname)
    print(hostname, ip_address)
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is ready to receive")

    while True:
        # Set up a new connection from the client
        client_socket, addr = server_socket.accept()
        # Handle the client's request
        handle_request(client_socket)

    # Close the server socket
    server_socket.close()

if __name__ == "__main__":
    server_port = 6799
    start_server(server_port)

