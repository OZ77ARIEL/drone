# Python Program to Get IP Address
import socket

def find_tello_ip(number_tello):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    octets = IPAddr.split('.')
    ip_list = []

    for i in range(1, 255):
        if i%25 == 0:
            print(f"searching, i={i}")
        if i == int(octets[3]):
            continue

        tello_ip = octets[0] + '.' + octets[1] + '.' + octets[2] + '.' + str(i)

        tello_port = 8889

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Bind the socket to a local port (you can choose any available port)
        local_port = 9000
        sock.bind(('0.0.0.0', local_port))

        # Send a command to the Tello drone
        command = "command"  # You can send other Tello commands as needed
        sock.sendto(command.encode(), (tello_ip, tello_port))

        # Set a timeout of 0.5 seconds for receiving a response
        sock.settimeout(0.15)

        try:
            # Receive and print the response
            response, _ = sock.recvfrom(1024)
            if response.decode() == "ok":
                print("Response:", response.decode(), "from IP:", tello_ip)
                ip_list.append(tello_ip)

        except socket.timeout:
            pass

        # Close the socket
        sock.close()
    if len(ip_list) == number_tello:
        return ip_list
    else:
        print(f"find {len(ip_list)} tello, not {number_tello} tello")
        return None

find_tello_ip(3)
