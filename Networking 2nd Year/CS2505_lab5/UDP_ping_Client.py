# UDP_ping_Client.py
from socket import * 
import sys
import time
import statistics

def client(server_ip, server_port, num_pings):
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.settimeout(1)  # Set socket timeout to 1 second
    print(f"Pinging {server_ip} with {num_pings} packets:")

    rtt_times = []

    for i in range(1, num_pings + 1):
        try:
            message = f"Ping {i} {int(time.time() * 1000)}"
            start_time = time.time()
            client_socket.sendto(message.encode(), (server_ip, server_port))
            response, server_address = client_socket.recvfrom(1024)
            end_time = time.time()
            rtt = (end_time - start_time) * 1000
            rtt_times.append(rtt)
            print(f"Received response from {server_address[0]}: udp_seq={i} time={rtt:.3f} ms")
        except timeout:
            print(f"Request timed out.")
        # except KeyboardInterrupt:
        #     break

    client_socket.close()

    if rtt_times:
        packet_loss = (num_pings - len(rtt_times)) / num_pings * 100
        print(f"\n--- {server_ip} ping statistics ---")
        print(f"{num_pings} packets transmitted, {len(rtt_times)} packets received, {packet_loss:.2f}% packet loss")
        print(f"round-trip min/avg/max/stddev = {min(rtt_times):.3f}/{statistics.mean(rtt_times):.3f}/{max(rtt_times):.3f}/{statistics.stdev(rtt_times):.3f} ms")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: UDP_ping_Client.py <number_of_pings> <server_ip>")
        sys.exit(1)

    num_pings = int(sys.argv[1])
    server_ip = sys.argv[2]
    client_port = int(input("Enter the port number: "))

    client(server_ip, client_port, num_pings)
