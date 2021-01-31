import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    message = int(input("tcpClientA: Enter message/ Enter exit:")) 
    print >>sys.stderr, 'sending "%d"' % message
    sock.send(str(message).encode('utf8'))
    

    
    data = sock.recv(1024)
       
    strings = data.decode('utf8')
    #get the num
    num = int(strings)
    print >>sys.stderr, 'received "%d"' % num
    data = sock.recv(16)
      

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()