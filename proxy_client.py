"""
Module that runs a client that sends a request to the proxy server.

Based on code from client.py on eClass.
"""


import socket


BUFFER_SIZE = 4096


def send_request(address, request):
    """Send a request to a given server.
    
    Params:
        address - (IP, Port) the address of the server to send the request to
        request - the bytes to send
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.connect(address)
        sc.sendall(request.encode())
        sc.shutdown(socket.SHUT_WR)
        data = sc.recv(BUFFER_SIZE)
        while data:
            print(data)
            data = sc.recv(BUFFER_SIZE)


def main():
    """Send a request to the proxy server."""

    proxy_address = "localhost", 8080
    host = "www.google.com"
    request = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'

    send_request(proxy_address, request)


if __name__ == "__main__":
    main()
