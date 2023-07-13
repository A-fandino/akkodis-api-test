import socket
from .server import UDP_PORT


def udp_client(data):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data_bytes = str(data).encode("utf-8")

    client.sendto(data_bytes, ("127.0.0.1", UDP_PORT))
