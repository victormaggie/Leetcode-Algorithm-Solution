
// use queue to update the dijstra

#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

typeof pair<int, int> PII; // <distance to starting poin, num of node>

N = 150010;
int n, m;
int h[N], e[N], ne[N], idx, w[N];
int dist[N];
bool st[N];

void add(int a, int b, int c) {
	e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx++;
}

int dijstra()
{
	memset(dist, 0x3f, sizeof dist);
	// the starting point , distance 0
	dist[1] = 0;
	// initialize the priority queue
	priority_queue<PII, vector<PII>, greater<PII>> heap;
	heap.push({0, 1});
	
	while (heap.size()){
		auto t = heap.top();
		heap.pop();
		
		// use the queue to get the node of smallest distance to the start
		int ver = t.second, distance = t.first;
		
		if (st[ver]) continue;
		st[ver] = true;
		
		// 
		for (int i = h[t]; i != -1; i = ne[i])
		{
			int j = e[i];
			if (dist[j] > distance + w[i])
			{
				dist[j] = distance + w[i];
				heap.push({dist[j], j});
			}
		}
	}
	if (dist[n] == 0x3f3f3f3f) return -1;
	return dist[n];
}

int main()
{
	memset(h, -1, sizeof h);
	cin >> n >> m;
	while (m--){
		int a, b, c;
		cin >> a >> b >> c;
		add(a, b, c);
	}
	cout << dijstra() << endl;
	return 0;	
}

















