#include <stdio.h>
int main(){
    int d, ano, mes, dia;
    scanf("%i",&d);
    ano = (int) d/365;
    mes = (int) (d%365)/30;
    dia = (int) (d%365%30);
    printf("%i ano(s)\n%i mes(es)\n%i dia(s)\n", ano, mes, dia);

    return 0;
}
