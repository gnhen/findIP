import socket


def get_wifi_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(ip_address)
    except socket.error as e:
        print(f"Error retrieving IP address: {e}")


if __name__ == "__main__":
    get_wifi_ip()
