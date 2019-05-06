#include <stdio.h>

int main(){
    int n, n100, n50, n20, n10, n5, n2, n1;
    scanf("%i", &n);
    printf("%i\n",n);
    n100 = (int) n/100;
    n50 = (int) ( (n - (n100*100) ) /50);
    n20 = (int) ( n - (n100*100) - (n50*50) )/ 20;
    n10 = (int) ( n - (n100*100) - (n50*50) - (n20*20) )/10;
    n5 = (int) ( n - (n100*100) - (n50*50) - (n20*20) - (n10*10) )/5;
    n2 = (int) ( n - (n100*100) - (n50*50) - (n20*20) - (n10*10) - (n5*5) )/2;
    n1 = (int) ( n - (n100*100) - (n50*50) - (n20*20) - (n10*10) - (n5*5) - (n2*2) )/1;
    printf("%i nota(s) de R$ 100,00", n100);
    printf("\n%i nota(s) de R$ 50,00", n50);
    printf("\n%i nota(s) de R$ 20,00", n20);
    printf("\n%i nota(s) de R$ 10,00", n10);
    printf("\n%i nota(s) de R$ 5,00", n5);
    printf("\n%i nota(s) de R$ 2,00", n2);
    printf("\n%i nota(s) de R$ 1,00\n", n1);

    return 0;
}
