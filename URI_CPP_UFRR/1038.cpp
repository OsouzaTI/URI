#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    int n,q;
    float p[] = {4.00,4.50,5.00,2.00,1.50};
    cin >> n >> q;
    cout << fixed << setprecision(2);
    cout << "Total: R$ " << p[n-1] * q << endl;

    return 0;
}
