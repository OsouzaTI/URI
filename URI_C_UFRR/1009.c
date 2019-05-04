#include <stdio.h>
 
int main() {
 
	char nome[30];
	double sf,vd,total;
	scanf("%s %lf %lf",&nome,&sf,&vd);
	total = sf + ( vd * ((double) 15/100) );
 	printf("TOTAL = R$ %.2lf\n",total);
    return 0;
}
