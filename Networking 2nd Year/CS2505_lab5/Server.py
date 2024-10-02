from socket import * 
import random

def simulate_packet_loss():
    # Simulate packet loss by randomly dropping packets
    # If it's more than 50% then drop the packet
    if random.randint(0, 100) >= 50:
        return True 
    else:
        return False
    
def server():
    hostname = gethostname()
    ip_address = gethostbyname(hostname)
    port = int(input("Enter the port number: "))

    # Create a UDP socket
    server_socket = socket(AF_INET, SOCK_DGRAM)

    # Bind the socket to a specific port number
    server_address = ("", port)
    server_socket.bind(server_address)

    print(f"Server is running on Host: {hostname} | IP: {ip_address} | Port: {port}")

    while True:
        try: 
            # Receive a message from the client
            data, client_address = server_socket.recvfrom(1024)

            # Simulate packet loss
            if simulate_packet_loss() == False: # no packet loss
                # Send the message back to the client
                server_socket.sendto(data, client_address)
                print('Sent message back to the client')
            else:
                print('Packet loss occurred, message dropped')
        except ConnectionResetError as e:
            pass
    
    # Close the socket
    server.close()

if __name__ == '__main__':
    server()