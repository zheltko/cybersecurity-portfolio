import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))
    sock.close()

    if result == 0:
        print(f"[OPEN] {host}:{port}")
    else:
        print(f"[CLOSED] {host}:{port}")


if __name__ == "__main__":
    target = "127.0.0.1"

    print("Scanning ports on", target)

    for port in range(20, 1025):
        check_port(target, port)
        