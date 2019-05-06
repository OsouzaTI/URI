#include<stdio.h>
#include<math.h>

int main(){
//NOTAS
int n1, n100, n50, n50_1, n20, n20_1, n10, n10_1, n5, n5_1, n2, n2_1;
//MOEDAS
int moedas, m1, m1_1, m50, m25, m10, m5, m01;

double n;

scanf("%lf", &n);
n1 = (int)n;
n -= n1;

moedas = (n *100);

n100 = n1/100;
n50 = n1 %100;
n50_1 = n50/50;
n20 = n50%50;
n20_1 = n20/20;
n10 = n20%20;
n10_1 = n10/10;
n5 = n10%10;
n5_1 = n5/5;
n2 = n5%5;
n2_1 = n2/2;
// MOEDAS
m1 = n2%2;
m1_1 = m1/1;

//NOTAS
printf("NOTAS:\n");
printf("%d nota(s) de R$ 100.00\n",n100);
printf("%d nota(s) de R$ 50.00\n",n50_1);
printf("%d nota(s) de R$ 20.00\n",n20_1);
printf("%d nota(s) de R$ 10.00\n",n10_1);
printf("%d nota(s) de R$ 5.00\n",n5_1);
printf("%d nota(s) de R$ 2.00\n",n2_1);


//MOEDAS
m50 = moedas /50;
m25 = (moedas %50)/25;
m10 = (((moedas %50)%25)/10);
m5 = ((((moedas %50)%25)%10)/5);
m01 = ((((moedas %50)%25)%10)%5)/1;

printf("MOEDAS:\n");
printf("%d moeda(s) de R$ 1.00\n", m1_1);
printf("%d moeda(s) de R$ 0.50\n", m50);
printf("%d moeda(s) de R$ 0.25\n", m25);
printf("%d moeda(s) de R$ 0.10\n", m10);
printf("%d moeda(s) de R$ 0.05\n", m5);
printf("%d moeda(s) de R$ 0.01\n", m01);

return 0;
}
