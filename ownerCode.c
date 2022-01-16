#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#define SIZE 1024


//INSERT THE NEW SHOES IN FILE
void function_Insert(){
	
	char typ[100],size[100],price[100];
	FILE *fptr;

	//ERROR HERE
	// fptr = fopen("shoesList","w");

	// if(fptr == NULL)
	// {
	  // printf("Error!");   
	  // exit(1);             
	// }
	
	// printf("Type of shoes : ");
	// scanf("%s",&typ);
	// printf("Size of shoes : ");
	// scanf("%s",&size);
	// printf("Price of shoes :RM  ");
	// scanf("%s",&price);

	// fprintf(fptr,"%s %s %s",type,siz,price);
	// fclose(fptr);
	
}

//DELETE THE SELECTED SHOES IN FILE
void function_Delete(){
	
}

//SHOW LIST OF SHOES IN FILE
void function_showList(){
	
	//ERROR HERE
	char c[1000];
    FILE *fptr;
    if((fptr = fopen("shoesList.txt", "r")) == NULL) {
        printf("Error! File cannot be opened.");
        exit(1);
    }
	else{
		//reads text until newline is encountered
		fscanf(fptr, "%[^\n]", c);
		printf("Data from the file:\n%s", c);
		fclose(fptr);
	}
}

//DO SOME TASK FOR OWNER SHOP
void function_task(){
	
	char input;
	printf("** WELCOME TO THE SHOES SHOP FOR THE OWBER **\n\n");
	
	for(;;){
		printf("1 - INSERT NEW BRAND\n");
		printf("2 - DELETE NEW BRAND\n");
		printf("3 - SHOW LIST NEW BRAND\n");
		printf("4 - EXIT \n");
		printf("Enter your chooice : ");
		input = getchar();  
		
		//CANNOT READ INPUT//ERROR
		
		if(input == '1'){
			function_Insert();
		}
		else if(input == '2'){
			function_Delete();
		}
		else if(input == '3'){
			function_showList();
		}
		else if(input == '4'){
			printf("Your have exit the systems !!\n");
			break;
		}
		else{
			printf("Your enter wrong input !!\n");
		}
	}
}


//MAIN FUNCTION FOR OWNER SHOP
int main(int argc, char const *argv[]){

	int sockfd, e;
	struct sockaddr_in server_addr;

	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if(sockfd < 0) {
	perror("[-]Error in socket");
	exit(1);
	}
	printf("[+]Server socket created successfully.\n");
	server_addr.sin_addr.s_addr = inet_addr("192.168.56.108");
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(8888);;


	e = connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr));
	if(e == -1) {
		perror("Error in socket");
		exit(1);
	}
	printf("Connected to Server.\n");
	
	// DO TASK
	function_task();

	printf("Closing the connection.\n");
	close(sockfd);

	return 0;
}
