#include<string>
#include<stdlib.h>
#include<vector>
using namespace std;

class Solution{
    bool canCanstruct(string ransomNote, string magazine){
        vector<int> counts(128, 0);
        for (const char c: magazine)
            ++counts[c];
        for (const char c: ransomNote)
            if (--counts[c]<0) return false;
        return true;
    }
};