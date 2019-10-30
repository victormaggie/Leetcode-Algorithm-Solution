#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    vector<string> ans;
    vector<string> letterCasePermutation(string S) {
        dfs(S, 0);
        return ans;
    };
    
    void dfs(string S, int u)     
        {        
        if (u == S.size())
        {
            ans.push_back(S);
            return;
        }
        dfs(S, u+1);
        
        if (S[u] >= 'A')
        {
            S[u] ^= 32;
            dfs(S, u +1);
        }
    }
};