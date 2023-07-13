import socket
import logging

UDP_PORT = 15020
UDP_SERVER_ADDRESS = ("0.0.0.0", UDP_PORT)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("user.udp")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(UDP_SERVER_ADDRESS)

    while True:
        data, _ = server.recvfrom(1024)
        logger.info(f"User: {data.decode('utf-8')}")
