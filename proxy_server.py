import socket
from threading import Thread


BUFFER_SIZE = 4096


def create_request(data):
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


def start_threaded_server():
    address = "localhost", 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Bind and listen
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(address)
        s.listen(2)
        
        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            t = Thread(target=handle_connection, args=(conn,))
            t.start()


def handle_connection(conn):
    
    #recieve data, wait a bit, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    response = create_request(full_data)
    conn.sendall(response)
    conn.close()


def start_server():
    address = "localhost", 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Bind and listen
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(address)
        s.listen(2)
        
        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            handle_connection(conn)

def main():
    start_threaded_server()


if __name__ == "__main__":
    main()
