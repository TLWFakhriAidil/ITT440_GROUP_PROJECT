#include <unistd.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <time.h>
#define STAD struct sockaddr

//This functoin raad and display to and pass wo server
void funcRead(int sock_desc){	

	int MAX = 1000;
	char buff[MAX];
	int n;
	bzero(buff, sizeof(buff));
	
	for(;;){
		printf("*Welcome to shoes stock checker*\n\n");
		printf("Please enter your * SHOES BRAND * that you want to search : ");
		n = 0;
		
		if((buff[n++] = getchar()) != '1'){
			
			write(sock_desc, buff, sizeof(buff));
			bzero(buff, sizeof(buff));
			read(sock_desc, buff, sizeof(buff));
			printf("\nFrom server : %s\n", buff);
		}
		else{
			break;
		}
	}
}

//main code for connected between server and client code
int main(){
	
	int sock_desc;
	struct sockaddr_in server;
	char *message, server_reply[1000];

	// socket create and verification
	sock_desc = socket(AF_INET, SOCK_STREAM, 0);
	
	if (sock_desc == -1) {
		printf("Could not to create socket...\n");
		exit(0);
	}
	else{
		printf("Socket successfully created…\n");
		bzero(&server, sizeof(server));
	}
	
	// assign IP Adress for server and PORT that using in it
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = inet_addr("192.168.56.108");
	server.sin_port = htons(1717);

	// connect the client socket to server socket
	if (connect(sock_desc, (STAD*)&server, sizeof(server)) < 0){
		printf("Failed to connect with server...\n");
		exit(0);
	}
	else{
		printf("Successfully connected with server...\n");
	}
	
	// This funvtion to read
	funcRead(sock_desc);

	// close the socket
	close(sock_desc);
}
