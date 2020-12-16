#include<cstdio>

using namespace std;

int main() {
	
	int num, tm;
	double pay;
	
	scanf("%i%i%lf", &num, &tm, &pay);
	printf("NUMBER=%i\nSALARY = U$%.2lf", num, pay * tm);
	return 0;
	
}