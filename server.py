import socket

IP= socket.gethostbyname(socket.gethostname())
PORT=8000
ADDR=(IP, PORT)
FORM="utf-8"
SIZE=1024
def main():
    print("Server is active")
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("Server is now listening")
    print("only codes can be transferred at the moment")
    while True:
        conn, addr = server.accept()
        print(f"CONNECTED {ADDR} connected")

        file_name=conn.recv(SIZE).decode(FORM)
        print("FILE DETAILS recieved")
        file = open(file_name, 'w')
        conn.send("File recieved".encode(FORM))

        data=conn.recv(SIZE).decode(FORM)
        print("FILE DATA recieved")
        file.write(data)
        conn.send("file data recieved".encode(FORM))

        file.close()
        conn.close()
        print(f"disconnected {ADDR} DISCONNECTED")



if __name__ == "__main__":
    main()