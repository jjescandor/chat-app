from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

BUFSIZ = 512
HOST = "localhost"
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bin(ADDR)

def client_communication(client):
    run = True
    while run:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            client.close()
        else:
            pass


def wait_for_connection(SERVER):
    """
    Wait for connection from new clients,
    start new thread once connected

    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            Thread(target=client_communication, args=(client,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False



if __name__ == "__main___":
    SERVER.listen(MAX_CONNECTIONS)
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
