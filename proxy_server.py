import socket


def main():
    address = "www.google.com", 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.connect(address)
        sc.shutdown(socket.SHUT_WR)


if __name__ == "__main__":
    main()
