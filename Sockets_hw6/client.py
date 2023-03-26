import socket, threading


def sock_recieve():
    while True:
        data_in = sock.recv(1024)
        print(data_in.decode('utf8'))

sock = socket.socket()

host = '127.0.0.1'
port = 44444

addr = (host, port)
sock.connect(addr)

rec_thread = threading.Thread(target=sock_recieve)
rec_thread.start()

nick = input()

while True:
    data = input()
    if data == 'stop':
        sock.close()
    sock.send(f"{nick}: {data}".encode('utf8'))


