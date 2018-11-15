#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'      # The server's hostname or IP address
PORT = 65432            # The port to send data to on the server
mySensorReadings = 'go' # The application layer protoll


def readSensors():
    sensorReadings = input('Type sensor readings: ')
    return sensorReadings

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text = 'go'
    while mySensorReadings != 'q':
        mySensorReadings = readSensors()
        s.sendall(mySensorReadings.encode('utf-8'))
    s.close()