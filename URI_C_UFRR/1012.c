#include <stdio.h>
int main(){

    double a,b,c,val;
    scanf("%lf %lf %lf",&a,&b,&c);
    val = (a * c)/2;
    printf("TRIANGULO: %.3lf\n", val);
    val = 3.14159 * (c*c);
    printf("CIRCULO: %.3lf\n", val);
    val = ((a + b)*c)/2;
    printf("TRAPEZIO: %.3lf\n", val);
    val = b*b;
    printf("QUADRADO: %.3lf\n", val);
    val = a*b;
    printf("RETANGULO: %.3lf\n", val);
    return 0;
}
