from socket import *
import random

def run_server():
    server = socket(AF_INET, SOCK_DGRAM)
    hostname = gethostname()
    ip_address = gethostbyname(hostname)
    server_address = (ip_address, 6789)

    server.bind(server_address)

    print("Server is ready to receive on port 6789")

    while True:
        message, client_address = server.recvfrom(2048)
        print(f"Received message: {message.decode()}")

        # Simulate packet loss
        rand = random.randint(1, 10)
        if rand > 5:
            modified_message = message.decode().upper()
            server.sendto(modified_message.encode(), client_address)
        else:
            print("Simulating packet loss, not sending acknowledgment.")

if __name__ == "__main__":
    run_server()
