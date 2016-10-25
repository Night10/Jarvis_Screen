import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip