"""
Module containing a concurrent proxy server to google.com.

Based on code from echo_server.py from eClass.
"""

import socket
from threading import Thread


BUFFER_SIZE = 4096


def create_request(data):
    """Forward the request to the target server and return the response.
    
    Params:
        data - the incoming request to forward
    """
    address = "www.google.com", 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        # Send request
        sc.connect(address)
        sc.sendall(data)
        sc.shutdown(socket.SHUT_WR)

        # Read response
        response = b''
        data = sc.recv(BUFFER_SIZE)
        while data:
            response += data
            data = sc.recv(BUFFER_SIZE)

    return response


def start_threaded_server():
    """Run a concurrent proxy server that forwards requests to google.com
    and sends the response back to the client.
    """
    
    address = "localhost", 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Bind and listen
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(address)
        s.listen(2)
        
        # Continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            # Use threads to allow concurrent connections
            t = Thread(target=handle_connection, args=(conn,))
            t.start()


def handle_connection(conn):
    """Read the incoming request, forward it to the target server,
    and send the response to the client.
    
    Params:
        conn - the client socket
    """
    full_data = conn.recv(BUFFER_SIZE)
    response = create_request(full_data)
    conn.sendall(response)
    conn.close()


def start_server():
    """Run a single-threaded proxy server that forwards requests to google.com
    and sends the response back to the client."""
    
    address = "localhost", 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Bind and listen
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(address)
        s.listen(2)
        
        # Continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            handle_connection(conn)


def main():
    # start_server()
    start_threaded_server()


if __name__ == "__main__":
    main()
