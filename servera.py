import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)


letter = 'a'
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    
    try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
            
                print >>sys.stderr, 'received "%d"' % data
              
                print >>sys.stderr, 'sending data back to the client'
                 
                if data == 'a':
                        letter = 'z'
                        connection.send(letter)
                else if data == 'b':
                        letter = 'a'
                        connection.send(letter)
                else if data == 'c':
                        letter = 'b'
                        connection.send(letter)
                else if data == 'd':
                        letter = 'c'
                        connection.send(letter)
                else if data == 'e':
                        letter = 'd'
                        connection.send(letter)
                else if data == 'f':
                        letter = 'e'
                        connection.send(letter)
                else:
                        letter = 'no':
                        connection.send(letter)
                      
                print >>sys.stderr, 'no more data from', client_address
                break
                
    finally:
            # Clean up the connection
            connection.close()