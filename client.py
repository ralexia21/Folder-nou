import socket

HOST= '127.0.0.1'
PORT= 65432

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
print("connected")

while True:
    message= input("You: ")
    client.sendall(message.encode())

    data= client.recv(1024)
    print(f"server: {data.decode()}")
    