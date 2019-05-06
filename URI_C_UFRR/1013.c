#include <stdio.h>
int main(){

    int a,b,c,maiorAB;
    scanf("%i %i %i",&a,&b,&c);
    maiorAB = (a+b+abs(a-b))/2;
    if(maiorAB==a){
        if(a>c){
            printf("%i eh o maior\n",a);
        }else{
            printf("%i eh o maior\n",c);
        }
    }else{
        if(b>c){
            printf("%i eh o maior\n",b);
        }else{
            printf("%i eh o maior\n",c);
        }
    }

    return 0;
}

