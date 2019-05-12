#include <iostream>
using namespace std;
int main(){
    int n, n100, n50, n20, n10, n5, n2, n1;
    cin >> n;
    n100 = (int) n/100;
    n50 = (int) (n%100)/50;
    n20 = (int) ((n%100)%50)/20;
    n10 = (int) (((n%100)%50)%20)/10;
    n5 = (int) ((((n%100)%50)%20)%10)/5;
    n2 = (int) (((((n%100)%50)%20)%10)%5)/2;
    n1 = (int) ((((((n%100)%50)%20)%10)%5)%2)/0.998;
    cout << n << endl;
    cout << n100 << " nota(s) de R$ 100,00" << endl;
    cout << n50 << " nota(s) de R$ 50,00" << endl;
    cout << n20 << " nota(s) de R$ 20,00" << endl;
    cout << n10 << " nota(s) de R$ 10,00" << endl;
    cout << n5 << " nota(s) de R$ 5,00" << endl;
    cout << n2 << " nota(s) de R$ 2,00" << endl;
    cout << n1 << " nota(s) de R$ 1,00" << endl;
    return 0;
}
