#include <iostream>
using namespace std;
int main(){
	float a,b,c,a_,b_,c_;
	cin >> a >> b >> c;
	if (a > b && b > c || a == b && b> c || a == b && b == c){
	    a_ = a;
	    b_ = b;
	    c_ = c;
	}else if (a > c && c > b || a == c && c > b || a > c && c == b){
	    a_ = a;
	    b_ = c;
	    c_ = b;
	}else if (c > a && a > b || c == a && c > b || c > a && a == b){
	    a_ = c;
	    b_ = a;
	    c_ = b;
	}else if (c > b && b > a || c == b && b > a || c > b && b == a){
	    a_ = c;
	    b_ = b;
	    c_ = a;
	}else if (b > c && c > a || b == c && c > a || b > c && c == a){
	    a_ = b;
	    b_ = c;
	    c_ = a;
	}else if (b > a && a > c || b == a && a > c || b > a && a == c) {
	    a_ = b;
	    b_ = a;
	    c_ = c;
	}
	if(a_ >= (b_ + c_)){cout << "NAO FORMA TRIANGULO\n";}
	else{
	    if( (a_*a_) == (b_*b_) + (c_*c_) ){cout << "TRIANGULO RETANGULO\n";}
	    if( (a_*a_) > (b_*b_) + (c_*c_) ){cout << "TRIANGULO OBTUSANGULO\n";}
	    if( (a_*a_) < (b_*b_) + (c_*c_) ){cout << "TRIANGULO ACUTANGULO\n";}
	    if( a_==b_ && b_==c_ ){cout << "TRIANGULO EQUILATERO\n";}
	    else if( a_==b_ ){cout << "TRIANGULO ISOSCELES\n";}
	    else if( a_==c_ ){cout << "TRIANGULO ISOSCELES\n";}
	    else if( b_==c_ ){cout << "TRIANGULO ISOSCELES\n";}
	}

	return 0;
}
