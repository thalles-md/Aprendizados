#include <stdio.h>

int main() {
	
	int age;
	printf("Digite sua idade: ");
	scanf("%d", &age);
	(age >= 18) ? printf("You can vote.\n") : printf("You cannot vote.\n");

}
