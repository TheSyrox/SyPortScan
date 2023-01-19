import socket

url = input("Enter the website URL: ")

# Get the IP address of the website
ip = socket.gethostbyname(url)

# Dictionary of well-known services and their default ports
services = {
    "ftp": 21,
    "ssh": 22,
    "telnet": 23,
    "smtp": 25,
    "http": 80,
    "pop3": 110,
    "imap": 143,
    "https": 443,
    "mysql": 3306,
    "rdp": 3389
}

# Scan all ports from 1 to 65535
for port in range(1, 65535):
    try:
        # Try to connect to the port
        sock = socket.create_connection((ip, port), timeout=1)
        service = next((name for name, value in services.items() if value == port), None)
        if service:
            print(f"Port {port} is open and running {service} service.")
        else:
            print(f"Port {port} is open but the service is unknown.")
        sock.close()
    except:
        pass
