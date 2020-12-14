
// Dijkstra algorithm

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 510;
int n, m;
int g[N][N];  // dense graph use the adjacent matrix 
int dist[N];  // memo the distance to the starting point
bool st[N];   // get the optimal distance or not

int dijkstra() {
	
	// Initialization distance to the starting point as INF
	memset(dist, 0x3f, sizeof dist);
	
	// the starting point to itself as 0
	dist[1] = 0;
	
	// Iterate N times, find a shortest distance each time.
	for (int i = 0; i < n; ++i) {
		int t = -1;
		for (int j = 1; j <= n; ++j) {
			// not in st , not update, or found another short distance
		if (!st[j] && (t == -1 || dist[j] < dist[t])) {
			t = j;
			}
		}
		// add to the st list
		st[t] = true;
		
		// find the smallest distance, and update the distance to t
		for (int j = 1; j <= n; ++j) {
			dist[j] = min(dist[j], dist[t] + g[t][j]);
		}
	}
	
	// if cannot reach n node, return -1
	if (dist[n] == 0x3f3f3f3f) return -1;
	
	return dist[n];
}


int main() {
	
	cin >> n >> m;
	
	memset(g, 0xf, sizeof g);
	
	while (m--) {
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		g[a][b] = min(g[a][b], c);
	};
	
	cout << dijkstra() << endl;
	return 0;
	
}