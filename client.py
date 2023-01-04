import socket, sys

IP= socket.gethostbyname(socket.gethostname())
PORT=8000
ADDR=(IP, PORT)
FORM="utf-8"
SIZE=1024

def main():
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
        
    file=open(sys.argv[1], "r")
    data=file.read()

    client.send(sys.argv[1].split('/')[-1].encode(FORM))
    msg=client.recv(SIZE).decode(FORM)
    print(f"msg: {msg}")

    client.send(data.encode(FORM))





if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("\n\t[RUN AS: ] python client.py /home/space-man/Documents/wall-e.txt\n")
        exit(0)
    except ConnectionRefusedError:
        print("\n\tServer is down\n")
