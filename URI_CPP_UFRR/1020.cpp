#include <iostream>

using namespace std;
int main(){
    int d, a, m, d_;
    cin >> d;
    a = (int) d/365;
    m = (int) (d%365)/30;
    d_ = (int) ((d%365)%30);
    cout << a << " ano(s)" << endl;
    cout << m << " mes(es)" << endl;
    cout << d_ << " dia(s)" << endl;

    return 0;
}
