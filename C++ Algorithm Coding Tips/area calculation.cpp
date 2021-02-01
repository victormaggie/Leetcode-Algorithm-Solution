#include <cstdio>
#include <cmath>

double PI = 3.14159;

int main() {
    
    double a, b, c;
    
    scanf("%lf%lf%lf", &a, &b, &c);
    
    printf("TRIANGULO: %.3lf\n", a * c / 2.);
    printf("CIRCULO: %.3lf\n", PI * pow(c, 2));
    printf("TRAPEZIO: %.3lf\n", (a + b) * c / 2.0);
    printf("QUADRADO: %.3lf\n", pow(b, 2));
    printf("RETANGULO: %.3lf\n", a * b);
    
    return 0;
}

// all the area value calculation!