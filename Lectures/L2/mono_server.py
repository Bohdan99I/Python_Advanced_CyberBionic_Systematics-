import socket

HOST = "127.0.0.1"
PORT = 50500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print(f"connection by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
            conn.sendall(data)
