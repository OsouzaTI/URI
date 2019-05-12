#include <stdio.h>
int main(){
	int n,i;
	scanf("%i",&n);
	float n1,n2,n3,arr[n];
	for(i;i<n;i++){
		scanf("%f %f %f",&n1,&n2,&n3);
		arr[i] = (n1*2+n2*3+n3*5)/10;
	}
	for(i=0;i<n;i++){
		printf("%.1f\n",arr[i]);
	}
	return 0;
}
