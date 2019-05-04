#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    double raio,area;
    cin >> raio;
    area = 3.14159 * (raio*raio);
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;
    return 0;
}
