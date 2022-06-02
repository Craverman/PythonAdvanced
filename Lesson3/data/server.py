import socket
import variables


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((variables.HOST, variables.PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
