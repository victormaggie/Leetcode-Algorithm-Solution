#include<string>
using namespace std;
class Solution{
public:
    string longestPalindrome(string s){
        string res;
        for (int i = 0; i < s.size(); i++){
            for (int j = i, k = i; j >= 0 && k < s.size() && s[j] == s[k]; j--, k++)
                if (res.size() < k - j + 1)
                    res = s.substr(j, k - j + 1);
            for (int j = i, k = i+1; j>= 0 && k < s.size() && s[j] == s[k]; j--, k++)
                if (res.size() < k - j + 1)
                    res = s.substr(k - j + 1);
    }
    return res;
    }
};

// time complexity o(n^2)
// space complexity o(1)
