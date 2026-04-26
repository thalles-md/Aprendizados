#include <stdio.h>
// Começando a mecher com Switch.

int main() {
	
	int number;
	printf("Digite um número: ");
	scanf("%d", &number);
	
	switch(number) {
	case 1:
	printf("Domingo.\n");
	break;

	case 2:
	printf("Segunda.\n");
	break;

	case 3:
	printf("Terça.\n");
	break;

	}
	return 0;
}
