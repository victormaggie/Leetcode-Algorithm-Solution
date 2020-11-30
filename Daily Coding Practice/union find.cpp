#include<vector>

using namespace std;

public:
 int find(int x){
    while (x != parent[x]){
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

public int find(int x){
    if (parent[x] != x){
        parent[x] = find(parent[x]);
    }
    return parent[x];
}