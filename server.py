import socket
import select
import sys
from thread import *
 
# AF_INET - address domain of socket 
# SOCK_STREAM - type of socket that data or characters are read in a continuous flow.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
# checks to see if proper 3 inputs are given
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
 
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port)) 
server.listen(100)
list_of_clients = []
 
def clientthread(conn, addr):
 
    # sends a message to the client whose user object is conn
    conn.send("Welcome to this chatroom!")
 
    while True:
            try:
                message = conn.recv(2048)
                if message:
 
                    """prints message and address of user 
                    who sent message on the server terminal"""
                    print "<" + addr[0] + "> " + message
                    """send message to all with broadcast"""
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send, conn)
 
                else:
                    """remove the connection"""
                    if conn in list_of_clients:
                        list_of_clients.remove(conn)
 
            except:
                continue
 
"""broadcast the message to clients who's connection is not 
the same as the one sending the message """
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
 
                """if the link is broken, we remove the object from the list
                 that was created at the beginning of the program"""
                if clients in list_of_clients:
                        list_of_clients.remove(clients)
 
while True:
     # conn - socket object
     # addr - contains IP address of client that just connected
    conn, addr = server.accept()
 
    # list of clients
    list_of_clients.append(conn)
 
    # print address of user that connected
    print addr[0] + " connected"
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()echo # lanchat-baljot4
