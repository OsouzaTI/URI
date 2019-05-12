#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    int h, kh;
    cin >> h >> kh;
    cout << fixed << setprecision(3);
    cout << (float) (h * kh)/12 << endl;
    return 0;
}

