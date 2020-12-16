#include<cstdio>
#include<cmath>

using namespace std;

int main(){
	double a1, a2, b1, b2;
	scanf("%lf%lf%lf%lf", &a1, &a2, &b1, &b2);
	print("%.4lf", sqrt(pow(a1 - b1, 2) + pow(a2 - b2, 2)));
	return 0;
}
