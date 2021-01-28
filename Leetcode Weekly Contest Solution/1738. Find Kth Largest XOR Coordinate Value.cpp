
const int N = 1000001;
int q[N];

class Solution {
public:
    int kthLargestValue(vector<vector<int>>& w, int k) {
        
        int n = w.size(), m = w[0].size();
        int cnt = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                
                if (i) w[i][j] ^= w[i-1][j];
                if (j) w[i][j] ^= w[i][j-1];
                if (i && j) w[i][j] ^= w[i-1][j-1];
                q[cnt++] = w[i][j];
            }
        }
            
        k = cnt - k;
        nth_element(q, q+k, q+cnt);
        return q[k];
    }
};