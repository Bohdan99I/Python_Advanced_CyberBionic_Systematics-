import socket

HOST = "127.0.0.1"
PORT = 50500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall("Hello, server!".encode("utf-8"))
    while True:
        data_out = sock.recv(1024)
        print(f"recived data: {data_out.decode('utf-8')}")
        data_in = input("Input text: ").encode("utf-8")
        if not data_in:
            break
        sock.sendall(data_in)
