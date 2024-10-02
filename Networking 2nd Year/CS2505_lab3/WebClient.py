import sys
from socket import *

def http_client(server_host, server_port, filename):
    # Create a TCP socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))

        # Construct the HTTP GET request
        request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"

        # Send the request to the server
        client_socket.sendall(request.encode())

        # Receive the server's response
        response = b""
        while True:
            # Receive data from the server
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        # Print the server's response
        print(response.decode())

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 client.py server_host server_port filename")
        sys.exit(1)

    # Parse command-line arguments
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    slash = "/"
    filename = slash + filename

    # Call the HTTP client function
    http_client(server_host, server_port, filename)