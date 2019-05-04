#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;
int main(){
    double r,total;
    cin >> r;
    total = (double)4/3 * 3.14159 * pow(r,3);
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << total << endl;
    return 0;
}


