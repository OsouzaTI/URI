#include <iostream>

using namespace std;
int main(){
    int s, h, m, s_;
    cin >> s;
    h = (int) s/3600;
    m = (int) (s%3600)/60;
    s_ = (int) ((s%3600)%60)%60;
    cout << h << ":" << m << ":" << s_ << endl;

    return 0;
}
