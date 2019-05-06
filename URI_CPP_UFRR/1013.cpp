#include <iostream>
#include <stdlib.h>

using namespace std;
int main(){	
	int a,b,c,maiorAB;
	cin >> a >> b >> c;
	maiorAB = ( a+b + abs(a-b) )/2;
	if(maiorAB == a){
		if(a > c){
			cout << a << " eh o maior" << endl;
		}else{
			cout << c << " eh o maior" << endl;
		}
	}else{
		if(b > c){
			cout << b << " eh o maior" << endl;
		}else{
			cout << c << " eh o maior" << endl;
		}
	}
	return 0;
}
