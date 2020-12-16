
#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int money;
	int stocks[] = {100, 50, 20, 10, 5, 2, 1};
	cin >> money;
	cout << money << endl;
	
	for (auto stock : stocks) {
		int nums = floor(money / stock);
		cout << nums << " nota(s) de R$ " << stock << ",00" << endl;
		money %= stock;
	}
	
	return 0;
}