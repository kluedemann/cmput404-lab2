import socket
from threading import Thread
from echo_server import Server, ThreadedHandler

BUFFER_SIZE = 4096

class ProxyHandler:

    def handle(self, conn):
        #recieve data, wait a bit, then send it back
        full_data = conn.recv(BUFFER_SIZE)
        response = self.create_request(full_data)
        conn.sendall(response)
        conn.close()

    def create_request(self, data):
        address = "www.google.com", 80
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
            sc.connect(address)
            sc.sendall(data)
            sc.shutdown(socket.SHUT_WR)
            response = b''
            data = sc.recv(BUFFER_SIZE)
            while data:
                response += data
                data = sc.recv(BUFFER_SIZE)
        return response



def main():
    server = Server(ProxyHandler())
    server = Server(ThreadedHandler(ProxyHandler()))
    server.accept_connections()


if __name__ == "__main__":
    main()
