import socket

####### A SIMPLE ILLUSTRATION OF THE TCP SERVER #######

# The port number on which to listen for incoming
# connections.
PORT_NUMBER = 1235

# Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Associate the socket with the port
serverSock.bind(('', PORT_NUMBER)) 

# Start listening for incoming connections (we can have
# at most 100 connections waiting to be accepted before
# the server starts rejecting new connections)
serverSock.listen(100)
print("Waiting for clients to connect...")
	
	# Accept a waiting connection
cliSock, cliInfo = serverSock.accept()
print("Client connected from: " + str(cliInfo))
# Keep accepting connections forever
while True:
	# Receive the data the client has to send.
	# This will receive at most 1024 bytes
    cliMsg = cliSock.recv(1024)
    msg = cliMsg.decode()
    if msg == "quit":
        print("Closing Connection")
        cliSock.close()
        break
    
    strMsg = str(cliMsg).upper()
    print("Client sent " + str(cliMsg))
    cliSock.send(strMsg.encode())

# Hang up the client's connection
cliSock.close()	