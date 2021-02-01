
#include <cstdio>

int main() {
	
	scanf("%d%d%lf", &n1, &num1, &p1);
	scanf("%d%d%lf", &n2, &num2, &p2);
	
	printf("VALOR A PAGAR: R$ %.2lf", num1 * p1 + num2 * p2);
	
	return 0;
}
