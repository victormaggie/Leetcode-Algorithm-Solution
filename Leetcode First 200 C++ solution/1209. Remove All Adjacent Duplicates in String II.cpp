
// Remove All Adjacent Duplicates in String II

/*
s = 'abcd' ,  k = 2
*/

#include <vector>

using namespace std;

class Solution{
public:
	string removeDuplicates(string s, int k) {
		
		vector<int> counts(s.size());
		for (int i = 0; i < s.size(); ++i) {
			
			if (i == 0 || s[i] != s[i-1]) {
				counts[i] = 1;
			} else {
				counts[i] = counts[i-1] + 1;
				if (counts[i] == k) {
					s.erase(i - k + 1, k);
					i = i - k;
				}
			}
		}	
		return s;
	}	
}

