#include <stdio.h>
// Checar par/ímpar e imprimir.

int main() {

	int numero;
	printf("Digite um número: ");
	scanf("%d", &numero);
	
	(numero % 2 == 0) ? printf("O número é par.\n") : printf("O número é ímpar.\n");
}
