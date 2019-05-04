#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    string nome;
    int n,q,n1,q1;
    float v,v1,total;
    cin >> n >> q >> v >> n1 >> q1 >> v1;
    total = q * v + q1 * v1;
    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ "<< total << endl;
    return 0;
}

