import socket

HOST= '127.0.0.1'
PORT= 65432

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print("Server on")

conn,addr= server.accept()
print(f"client connected from {addr}")

while True:
    data= conn.recv(1024)
    if not data:
        break
    message = data.decode()
    print(f"client: {message}")

    reply= input("You: ")
    conn.sendall(reply.encode())

conn.close()

