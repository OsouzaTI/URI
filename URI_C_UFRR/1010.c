#include <stdio.h>
 
int main() {
 
	int n,q,n1,q1;
	float p,p1,total;
	scanf("%i %i %f",&n,&q,&p);
	scanf("%i %i %f",&n1,&q1,&p1);
	total = (q * p) + (q1 * p1);
	printf("VALOR A PAGAR: R$ %.2f\n",total);
	 
    return 0;
}
