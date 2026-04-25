#include <stdio.h>

int main() {

	double number;
	char alpha;

	printf("\nEnter double input: ");
	scanf("%lf", &number);

	printf("\nEnter a letra input: ");
	scanf("\n%c", &alpha);

	printf("\nCharacter: %c", alpha);
	printf("\nNumber: %lf", number);

	return 0;
}
