#include <stdio.h>

int main(){
    int s, horas, minutos, segundos;
    scanf("%i",&s);
    horas = (int) s/3600;
    minutos = (int) ((s%3600)/60);
    segundos = (s%3600)%60;
    printf("%i:%i:%i",horas,minutos,segundos);

    return 0;
}

