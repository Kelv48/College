# UDP_ping_Server.py
import socket
import random
import time

def server(port, loss_rate):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))
    print("Server ready to receive pings...")

    while True:
        try:
            message, client_address = server_socket.recvfrom(1024)
            if random.random() < loss_rate:
                continue  # Simulate packet loss
            current_time = int(time.time() * 1000)
            server_socket.sendto(f"Pong {message.decode()} {current_time}".encode(), client_address)
        except KeyboardInterrupt:
            print("\nServer terminated.")
            break
    server_socket.close()

if __name__ == "__main__":
    server_port = 12000
    loss_rate = 0.3  # 30% packet loss rate
    server(server_port, loss_rate)
 