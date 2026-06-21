import socket
import threading

HOST = '0.0.0.0'
PORT = 5001

def get_line(line_id):
    with open('data.txt', 'r') as f:
        for line in f:
            if line.startswith(str(line_id) + ','):
                return line.strip()
    return 'NOT FOUND'

def handle_client(conn):
    request = conn.recv(1024).decode().strip()
    response = get_line(request)
    conn.send(response.encode())
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print('Multi-threaded server (thread per request) running on port ' + str(PORT))

while True:
    conn, addr = server.accept()
    t = threading.Thread(target=handle_client, args=(conn,))
    t.start()
