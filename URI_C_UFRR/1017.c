#include <stdio.h>

int main(){
    int h,kh;
    float total;
    scanf("%i %i",&h,&kh);
    total = (float) (h * kh)/12;
    printf("%.3f\n", total);

    return 0;
}
