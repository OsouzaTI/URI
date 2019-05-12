#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int n, n100, n50, n20, n10, n5, n2, n1;
    float n_;
    cin >> n_;
    n = (int) n_;
    n100 = (int) n/100;
    n50 = (int) (n%100)/50;
    n20 = (int) ((n%100)%50)/20;
    n10 = (int) (((n%100)%50)%20)/10;
    n5 = (int) ((((n%100)%50)%20)%10)/5;
    n2 = (int) (((((n%100)%50)%20)%10)%5)/2;
    //n1 = (int) ((((((n%100)%50)%20)%10)%5)%2)/0.998;
    cout << "NOTAS:" << endl;
    cout << n100 << " nota(s) de R$ 100.00" << endl;
    cout << n50 << " nota(s) de R$ 50.00" << endl;
    cout << n20 << " nota(s) de R$ 20.00" << endl;
    cout << n10 << " nota(s) de R$ 10.00" << endl;
    cout << n5 << " nota(s) de R$ 5.00" << endl;
    cout << n2 << " nota(s) de R$ 2.00" << endl;
    int m,m100,m50,m25,m10,m5,m1;
    m = (ceil((n_ - (n100*100+n50*50+n20*20+n10*10+n5*5+n2*2))*1000)*.001)*100;
    m100 = (int) m/100;
    m50 = (int) (m%100)/50;
    m25 = (int) ((m%100)%50)/25;
    m10 = (int) (((m%100)%50)%25)/10;
    m5 = (int) ((((m%100)%50)%25)%10)/5;
    m1 = (int) (((((m%100)%50)%25)%10)%5)/0.9;
    cout << "MOEDAS:" <<endl;
    cout << m100 << " moeda(s) de R$ 1.00" <<endl;
    cout << m50 << " moeda(s) de R$ 0.50" <<endl;
    cout << m25 << " moeda(s) de R$ 0.25" <<endl;
    cout << m10 << " moeda(s) de R$ 0.10" <<endl;
    cout << m5 << " moeda(s) de R$ 0.05" <<endl;
    cout << m1 << " moeda(s) de R$ 0.01" <<endl;
    return 0;
}

