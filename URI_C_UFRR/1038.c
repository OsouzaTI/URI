#include <stdio.h>

int main(){
    int a,b;
    scanf("%i %i",&a,&b);
    float c[] = {4.00,4.50,5.00,2.00,1.50};
    printf("Total: R$ %.2f\n", c[a-1] * b);

    return 0;
}

