import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    message = raw_input("Enter message/ Enter exit:") 
    print >>sys.stderr, 'sending "%d"' % message
    sock.send(message)
    

    
    data = sock.recv(16)
       
    print >>sys.stderr, 'received "%s"' % data
    data = sock.recv(16)
      

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()