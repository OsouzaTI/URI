#include <stdio.h>
int main(){
    int a,b,c,d;
    scanf("%i %i %i %i",&a,&b,&c,&d);
    if(b > c && d > a && (c + d) > (a + b) && c > 0 && d > 0){
        printf("Valores aceitos");
    }else{
        printf("Valores nao aceitos");
    }

    return 0;
}
