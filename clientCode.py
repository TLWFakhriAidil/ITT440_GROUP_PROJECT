#client code
import socket

ClientSocket = socket.socket()
host = '192.168.56.108'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)

while (True):
    print('\n *Welcome To The Client*\n')
    print('\n1) Search Shoes Brand')#ERROR CANNOT DO COMPARISON
    print('2) Exit')
    choice=input('Enter your choice : ')

    if choice == '1':
        print('\n')
        brand=input('Enter Shoes Brand : ')
        saiz=input('Enter Shoes Saiz : ')
        price=input('Enter Shoes Price : RM ')
        choice='5'

        passReply1= choice+','+brand+','+saiz+','+price
        ClientSocket.send(str.encode(passReply1))
        Response=ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

        choiceClient=input('Your Input : ')
        passReply1= choiceClient
        ClientSocket.send(str.encode(passReply1))
        Response=ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        
    if choice == '2':
        print('Thank You For Using The System')
        break
ClientSocket.close()