#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main(){
    double a,b,c,delta;
    cin >> a >> b >> c;
    delta = (b*b) - 4 * a * c;
    if(delta > 0 && a != 0){
        cout << fixed << setprecision(5);
        cout << "R1 = "<< (-b + sqrt(delta))/(2*a) << endl;
        cout << "R2 = "<< (-b - sqrt(delta))/(2*a) << endl;
    }else if(delta < 0 or a == 0){
        cout << "Impossivel calcular" << endl;
    }

    return 0;
}

