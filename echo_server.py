#!/usr/bin/env python3

"""
Module containing code to run a concurrent echo server.

Modified from echo_server.py code on eClass.
"""

import socket
import time
from threading import Thread

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def handle_connection(conn):
    """Send the data back to the client after a brief delay.
    
    Params:
        conn - the client socket
    """
    SLEEP_TIME = 0.5

    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(SLEEP_TIME)
    print(full_data)
    conn.sendall(full_data)
    conn.close()


def main():
    """Run the threaded echo server."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            # Non-threaded version:
            # handle_connection(conn)

            # Use threads to allow concurrent connections
            t = Thread(target=handle_connection, args=(conn,))
            t.start()


if __name__ == "__main__":
    main()
