#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    int n,h;
    float sh,total;
    cin >> n >> h >> sh;
    total = h * sh;
    cout << fixed << setprecision(2);
    cout << "NUMBER = " << n << endl;
    cout << "SALARY = U$ " << total << endl;
    return 0;
}
