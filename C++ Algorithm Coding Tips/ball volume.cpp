#include <cstdio>
#include <cmath>

double PI = 3.14159;

int main() {
    
    double R;
    
    scanf("%lf", &R);
    
    printf("VOLUME = %.3lf", PI * pow(R, 3) * (4 / 3.));
    
    return 0;
}

# calculate the volume of a ball;