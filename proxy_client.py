import socket


BUFFER_SIZE = 4096


def main():
    proxy_address = "localhost", 8080
    host = "www.google.com"
    request = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.connect(proxy_address)
        sc.sendall(request.encode())
        sc.shutdown(socket.SHUT_WR)
        data = sc.recv(BUFFER_SIZE)
        while data:
            print(data)
            data = sc.recv(BUFFER_SIZE)


if __name__ == "__main__":
    main()
