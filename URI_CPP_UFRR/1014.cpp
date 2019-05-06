#include <iostream>
#include <iomanip>
using namespace std;
int main(){	
	int km;
	float l;
	cin >> km >> l;
	cout << fixed << setprecision(3);
	cout << km/l << " km/l" << endl;
	return 0;
}
