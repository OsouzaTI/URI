#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    string nome;
    double sf,vd,total;
    cin >> nome >> sf >> vd;
    total = sf + (vd * (double) 15/100);
    cout << fixed << setprecision(2);
    cout << "TOTAL = R$ " << total << endl;
    return 0;
}

