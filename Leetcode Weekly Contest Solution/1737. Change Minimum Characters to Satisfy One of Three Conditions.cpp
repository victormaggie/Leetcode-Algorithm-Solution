
class Solution {
	
public:
		
	int work(vector<int> s1, vector<int> s2) {
		
		int res = INT_MAX;
		for (int i = 1; i < 26; i++) {
			
			int cnt = 0;
			
			for (int j = i; j < 26; j++) cnt += s1[j];
			for (int j = 0; j < i; j++) cnt += s2[j];
			
			res = min(res, cnt);
		}
		
		return res;
	}
	
	int minCharacters(string a , string b) {
		
		vector<int> s1(26), s2(26);
		for (auto c: a) s1[c - 'a']++;
		for (auto c: b) s2[c - 'a']++;
		
		int n = a.size(), m = b.size();
		int res = INT_MAX;
		
		for (int i = 0; i < 26; i++) {
			res = min(res, n + m - (s1[i] + s2[i]));
		}
		
		return min(res, min(work(s1, s2), work(s2, s1)));
	}
}

