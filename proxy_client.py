import socket


def main():
    proxy_address = "localhost", 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.connect(proxy_address)
        sc.shutdown(socket.SHUT_WR)


if __name__ == "__main__":
    main()
