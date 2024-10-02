from socket import *
import select

def run_client():
    # DNS lookup for the server's IP address
    client = socket(AF_INET, SOCK_DGRAM)
    hostname = gethostname()
    ip_address = gethostbyname(hostname)
    port = 6789
    server_address = (ip_address, port)


    # Create a datagram socket and set it to non-blocking
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.setblocking(0)
    
    timeout = 1  # 1 second timeout

    # Open the file
    with open("testfile.txt", 'r') as file:
        for line in file:
            sent = False
            while not sent:
                # Send each line to the server
                client_socket.sendto(line.strip().encode(), (ip_address, port))
                ready = select.select([client_socket], [], [], timeout)
                
                if ready[0]:  # Data is ready to be read
                    modified_message, _ = client_socket.recvfrom(2048)
                    print(modified_message.decode())
                    sent = True
                else:
                    print("Timeout reached, resending...")

    client_socket.close()

if __name__ == "__main__":


    run_client()
