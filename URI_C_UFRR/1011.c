#include <stdio.h>
 
int main() {
 
	double n,total;
	scanf("%lf",&n);
	total = ( (double) 4/3 ) * 3.14159 * (n*n*n);
	printf("VOLUME = %.3f\n",total);
	 
    return 0;
}
