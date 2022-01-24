#client code
import socket

ClientSocket = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)

while (True):
    print('\n *Welcome To The Owner*\n')
    print('\n1) Insert New Brand')
    print('2) Show List Brand Shoes')
    print('3) Delete Shoes Brand')#ERROR CANNOT DO THE COMPARISON
    print('4) Calculation On Sale')#ERROR CANNOT READ INPUT DATA//EOF ERROR
    print('5) Exit')
    choice=input('Enter your choice : ')

    if choice == '1':
        print('\n')
        brand=input('Enter Shoes Brand : ')
        size=input('Enter Shoes Saiz : ')
        price=input('Enter Shoes Price : RM ')

        passReply1= choice+','+brand+','+size+','+price
        ClientSocket.send(str.encode(passReply1))
        Response=ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

    if choice == '2':
        passReply2= choice
        ClientSocket.send(str.encode(passReply2))
        Response=ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
            
    if choice == '3':
        print('\n')
        brand=input('The Brand That Owner Want To Delete: ')
        size=input('The Brand That Size Want To Delete: ')
        price=input('The Brand That Price Want To Delete: RM ')

        passReply3= choice+','+brand+','+size+','+price
        ClientSocket.send(str.encode(passReply3))
        Response=ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

    if choice == '4':
        passReply4= choice
        ClientSocket.send(str.encode(passReply4))
        Response=ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        
    if choice == '5':
        print('Thank For Using The Systems')
        break
ClientSocket.close()