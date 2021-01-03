
#include<algorithm>
#include<iostream>


// the size of the node
const N = 510;
int n, m;
// use the graph dense -> adjacent matrix
int g[N][N];
// The node is check or not
bool st[N];
// Check the answer of the system
int dist[N];


int Dijkstra() {
	
	memset(dist, 0x3f, sizeof dist);
	
	// initialize the starting node
	dist[1] = 0;
	
	// iterate all the node to find the next starting point
	for (int i = 1; i <= n; i++) {
		
		// check index
		int t = -1;
		for (int j = 1; j <= n; j++) {
			// node must not be selected
			if (!st[j] && ( t == -1 || dist[j] < dist[t]))
				// the next round we might select t node
				// greedy , each time we choose the smallest one
				// the assumption is  that the router cost will be positive_sign
				// we might not traveral all the node
				t = j;			
		}
		
		// select the j node here!
		st[t] = true;
		
		// here we need perform relaxation
		for (int i = 1; i <= n; i++) {
			// relaxation condition  --> Update the next adjacent list 
			// even though some node are not connect to the current selected node
			// but g[t][i] will be infinite, as such no hurts.!
			dist[i] = min(dist[i], dist[t] + g[t][i]);
		}
	}
	if (dist[n] == 0x3f) return -1;
	return dist[n];
	
}

int main() {
	
	cin >> n >> m;
	
	memset(g, 0x3f, sizeof g);
	
	
	while (m--) {
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		g[a][b] = min(g[a][b], c);
	}
	
	int t = dijkstra();
	printf("%d\n", t);
}



