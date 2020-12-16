#include<iostream>
#include<unordered_map>
#include<iomanip>

int main()
{
	int id, num;
	unordered_map<int, double> umap;
	cin >> id >> num;
	umap[1] = 4.0;
	umap[2] = 4.5;
	umap[3] = 5.0;
	umap[4] = 2.0;
	umap[5] = 1.5;
	printf("Total: R$ %.2f ", umap[id] * num);
	return 0;
}



/*

int main() {
	
	int x, y;
	scanf("%d%d", &x, &y);
	
	double p;
	switch (x) {
		
		case 1:
			p = 4.0 * y;
			break;
		case 2:
			p = 4.5 * y;
			break;
		case 3:
			p = 5.0 * y;
			break;
		case 4:
			p = 2.0 * y;
			break;
		case 5:
			p = 1.5 * y;
			break;
	}
	
	printf("Total: R$ %.2f", p);
	return 0;
	
}

*/