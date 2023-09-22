#!/usr/bin/env python3
import socket
import time
from threading import Thread


class Server:

    def __init__(self, handler) -> None:
        self.handler = handler

    def accept_connections(self):
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
                
                self.handler.handle(conn)


class EchoHandler:

    def handle(self, conn):
        full_data = conn.recv(BUFFER_SIZE)
        time.sleep(0.5)
        print(full_data)
        conn.sendall(full_data)
        conn.close()


class ThreadedHandler:

    def __init__(self, handler):
        self.handler = handler

    def handle(self, conn):
        #recieve data, wait a bit, then send it back
        t = Thread(target=self.handler.handle_connection, args=(conn,))
        t.start()


#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def main():
    server = Server(EchoHandler())
    server = Server(ThreadedHandler(EchoHandler))
    server.accept_connections()

if __name__ == "__main__":
    main()
