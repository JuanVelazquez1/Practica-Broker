import socket
import sys
import select
import errno
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

broker_address = ('localhost', 10000)
port = 10001

# Variable to control if the port selected is free
connected = False

# Bind the socket to the port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while not connected:
    try:
        server_address = ('localhost', port)
        sock.bind(server_address)
        connected = True
        print('starting up on {} port {}'.format(*server_address))
        
    # If bind gives an error, it means that the port is already in use
    # so we try with the next one, until one is free
    except socket.error as error:
        if error.args[0] == errno.EADDRINUSE:
            port += 1

messageA = b'sub:id:%i'%port
messageB = b'sub:topic:game'

try:
    # Send data
    print('sending {!r}'.format(messageA))
    sent = sock.sendto(messageA, broker_address)
    print('sending {!r}'.format(messageB))
    sent = sock.sendto(messageB, broker_address)
finally:
    print('closing socket')
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', port)
sock.bind(server_address)
while True:
    print('\nwaiting to receive message')
    rlist, _, _ = select.select([sock], [], []) 
    data, address = sock.recvfrom(1024)
    # Do stuff with data, fill this up with your code
    print('received {} bytes from {}'.format(len(data), address))
    print(data)


