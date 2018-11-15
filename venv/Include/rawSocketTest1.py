from rawsocketpy import RawSocket
sock = RawSocket('wlp2s0', 0xEEFA)
while True:
    print(sock.recv())