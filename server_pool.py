import socket
from concurrent.futures import ThreadPoolExecutor

HOST = '0.0.0.0'
PORT = 5002
POOL_SIZE = 4

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
print('Multi-threaded server (thread pool) running on port ' + str(PORT))

with ThreadPoolExecutor(max_workers=POOL_SIZE) as pool:
    while True:
        conn, addr = server.accept()
        pool.submit(handle_client, conn)
