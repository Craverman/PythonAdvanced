import socket
import variables

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((variables.HOST, variables.PORT))
    s.sendall(b"Hello, GeekBrains students")
    data = s.recv(1024)

print(f"Received {data!r}")
