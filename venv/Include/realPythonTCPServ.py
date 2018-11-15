#!/usr/bin/env python3
# TCP server. Will listen until client closes connection
# Adapted by Per dahlstrøm
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on: ',s)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(16)
            print(data.decode('utf-8'))
            if not data:
                break

            # conn.sendall(data)
