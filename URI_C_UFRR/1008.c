#include <stdio.h>
 
int main() {
 
	int n,h;
	float sh,total;
	scanf("%i %i",&n,&h);
	scanf("%f",&sh);
	total = h * sh;
	printf("NUMBER = %i\n",n);
	printf("SALARY = U$ %.2f\n",total);
 
    return 0;
}
