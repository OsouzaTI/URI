#include <iostream>
int main(){
	int a,b,temp;
	std::cin >> a >> b;
	temp = 0;
	if (a > b){
		temp = b;
	    b = a;
	    a = temp;	
	}	    
	if((b%a)==0){std::cout<<"Sao Multiplos\n";}
	else{std::cout<<"Nao sao Multiplos\n";}
	return 0;	
}

