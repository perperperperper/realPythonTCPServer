#!/usr/bin/env python3
# TCP client. Will send data until data is 'q' - quit
# Written by Per Dahlstrøm
# The program sends data every second. This is configurable
import socket, time, random
from socket import SHUT_WR

HOST = '127.0.0.1'      # The server's hostname or IP address
PORT = 65432            # The port to send data to on the server
mySensorReadings = 'go' # The application layer protoll


def readSensors():
    # mySensorReadings = input('Type sensor readings: ')
    mySensorReadings = str(random.randint(1, 100)) # generate random values
    return mySensorReadings

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

while mySensorReadings != 'q':
    mySensorReadings = readSensors()
    connection = connect()
    connection.sendall(mySensorReadings.encode('utf-8'))
    connection.shutdown(SHUT_WR)
    connection.close()
    time.sleep(1)