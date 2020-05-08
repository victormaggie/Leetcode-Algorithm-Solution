class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashset = set()
        for i in wordDict:
            hashset.add(i)
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)):
            for j in (i, -1, -1):
                subset = s[i-j:i+1]
                if subset in hashset:
                    if dp[i-j] == True:
                        dp[i] = True
                        break
        return dp[-1]
                    
        