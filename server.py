#code server
import socket
import sys
import time
import errno
import math
import os
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server\n'))

    #GET REPLY FROM CLEINT
    while (True):
        data=s_sock.recv(1024)
        print(data)
        data=data.decode('utf-8')
        try:
            value=data.split(',')
        except:
            print('Unable To Read')
        if not data:
            break
        print(value)
        
        if value[0] == '1':#FOR CODE OWNER INSERT
            
            print("The Command That Owner Choose : "+value[0])
            print('\n')

            value1=value[1]
            value2=value[2]
            value3=value[3]
            print("The Brand That Owner Input: "+value1)
            print("The Brand That Size Input: "+value2)
            print("The Brand That Price Input: RM "+value3)

            write_file=open('shoesList.txt','a')
            write_file.write(value1+','+value2+','+value3+'\n')
            
            replyServer='The Information Has been Store In File shoesList.txt'
            
            write_file.close()
            s_sock.send(str.encode(replyServer))

        if value[0] == '2':#FOR CODE OWNER SHOW LIST
            
            print("The Command That Owner Choose :"+value[0])

            show_file=open('shoesList.txt', 'r')

            readFile=show_file.read()
            replyServer = readFile

            show_file.close()
            s_sock.send(str.encode(replyServer))

        if value[0] == '3':#FOR CODE OWNER DELETE

            print("The Command That Owner Choose :"+value[0])
            print('\n')

            value1=value[1]
            value2=value[2]
            value3=value[3]
            print("The Brand That Owner Want To Delete: "+value1)
            print("The Brand That Size Want To Delete: "+value2)
            print("The Brand That Price Want To Delete: RM "+value3)

            counter_file=open('shoesList.txt', 'r')
            show_file=open('shoesList.txt', 'r')
            #delete_line=open('shoesList.txt', 'w')

            #THIS FOR COUNT
            count = 0
            content = counter_file.read()
            CoList = content.split('\n')
            for i in CoList:
                if i:
                    count = count + 1

            data = 0

            while(True):
                readFile=show_file.readline()
                L=readFile.split(',')

                if (data < count):
                    print('MASUK -1')
                    data = data + 1
                    L[2] = L[2].rsplit()#TO REMOVE '\n'
                    print('L[2] :' + L[2])
                    print('Value 3 :' +value3)

                    if str(L[0]) == value1:
                        print('MASUK -2')
                        if str(L[1]) == value2:
                            print('MASUK -3')
                            if str(L[2]) == value3:
                                print('MASUK -4')
                                
                                #L = L.rstrip()
                                #delete_line = L
                                #delete_line.pop()

                                replyServer= 'Successfully Deleted'
                                break
                else:
                    replyServer ='Not Successufully Deleted'
                    break

            counter_file.close()
            show_file.close()
            #delete_line.close()
            s_sock.send(str.encode(replyServer))

        if value[0] == '4':# FOR CODE OWNER CALCULATION

            print("The Command That Owner Choose :"+value[0])
            print('\n')

            count_BuyerShoes=open('buyer.txt', 'r')
            buyer_shoes=open('buyer.txt', 'r')
            
            # THIS FOR COUNT
            count = 0
            content = count_BuyerShoes.read()
            CoList = content.split('\n')
            for i in CoList:
                if i:
                    count = count + 1
            
            data = 0
            total = 0.00

            while(True):

                readFile=buyer_shoes.readline()
                L=readFile.split(',')
                print(L)

                if(data < count):

                    data = data + 1

                    L[2] = L[2].rstrip()#TO REMOVE '\n'
                    total = total + float(L[2])

                else:
                    break
            
            sumTotal = str(total)
            print('The total is : RM ')
            print(sumTotal)

            replyServer= sumTotal

            count_BuyerShoes.close()
            buyer_shoes.close()
            s_sock.send(str.encode(replyServer))

        if value[0] == '5':# FOR CODE CLIENT SEARCH

            print("The Command That Owner Choose :"+value[0])
            print('\n')

            value1=value[1]
            value2=value[2]
            value3=value[3]
            print("The Brand That Client Input: "+value1)
            print("The Size That Client Input: "+value2)
            print("The Price That Client Input: "+value3)

            counter_file=open('shoesList.txt', 'r')
            show_file=open('shoesList.txt','r')
            #delete_line=open('shoesList.txt', 'w')
            buyer_shoes=open('buyer.txt','a')

            #THIS FOR COUNT
            count = 0
            content = counter_file.read()
            CoList = content.split('\n')
            for i in CoList:
                if i:
                    count = count + 1

            data = 0

            while(True):
                readFile=show_file.readline()
                L=readFile.split(',')

                if (data < count):
                    print('MASUK -1')

                    data = data +1 
                    L[2] = L[2].rstrip()#TO REMOVE '\n'

                    if str(L[0]) == value1:
                        print('MASUK -2')
                        if str(L[1]) == value2:
                            print('MASUK -3')
                            if str(L[2]) == value3:
                                print('MASUK -4')

                                replyServer='Found The Shoes'+'\n Enter Y - Yes or N - No : '
                                s_sock.send(str.encode(replyServer))

                                #GET REPLY FORM CLIENT
                                data=s_sock.recv(1024)
                                print(data)
                                value=data.decode('utf-8')

                                if not value:
                                    replyServer = '!!!!You Enter The Wrong Input!!!!'
                                    break
                                print(value)

                                if (value == 'Y' or value == 'y'):

                                    buyer_shoes.write(value1+','+value2+','+value3+'\n')

                                    #L = L.rstrip()#TO REMOVE '\n'
                                    #delete_line = L
                                    #show_file.pop()#TO REMOVE THAT DATA

                                    replyServer = 'Your Purchase Has Successful, Thank For Using Our Systems'
                                    break

                                if (value == 'N' or value == 'n'):
                                    replyServer = 'Thank for Using the systems'
                                    break
                else:
                    replyServer = 'Do Not Found The Shoes'
                    break

            counter_file.close()
            show_file.close()
            #delete_line.close()
            buyer_shoes.close()
            s_sock.send(str.encode(replyServer))

    s_sock.close()

#THE MAIN CODE TO DO CONNECTION FOR THE CLIENT AND OWNER TO THE SERVER
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',8888))
    print('listening...')
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
           s.close()