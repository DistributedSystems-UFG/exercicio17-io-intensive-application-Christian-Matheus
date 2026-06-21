import socket
import time
import sys

HOST = '127.0.0.1'
REQUESTS = 100

def send_request(port, line_id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))
    s.send(str(line_id).encode())
    response = s.recv(1024).decode()
    s.close()
    return response

def benchmark(port, label):
    print('Testing ' + label + '...')
    start = time.time()
    for i in range(REQUESTS):
        line_id = (i % 10) + 1
        send_request(port, line_id)
    elapsed = time.time() - start
    rps = round(REQUESTS / elapsed, 2)
    print('  Requests: ' + str(REQUESTS))
    print('  Time: ' + str(round(elapsed, 2)) + 's')
    print('  Throughput: ' + str(rps) + ' req/s')
    print()

benchmark(5000, 'Single-threaded (port 5000)')
benchmark(5001, 'Multi-threaded per request (port 5001)')
benchmark(5002, 'Thread pool (port 5002)')
