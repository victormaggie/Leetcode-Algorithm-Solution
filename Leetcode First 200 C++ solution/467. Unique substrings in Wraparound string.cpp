class Solution {
public:
    int findSubstringInWraproundString(string p) {
        
        unordered_map<char, int> cnt;
        
        for (int i = 0; i < p.size();){
            int j = i + 1;
            
            while (j < p.size() && (p[j] - p[j-1] == 1 || p[j] == 'a' && p[j-1] == 'z'))  j++;
            while (i < j) cnt[p[i]] = max(cnt[p[i]], j - i), i ++;
        }
        
        int res = 0;
        for (auto[a, b]:cnt) res += b;
        return res;
    }
};