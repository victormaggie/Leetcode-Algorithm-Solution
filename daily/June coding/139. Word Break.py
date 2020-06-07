class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict: return False

        dp = [-1 for i in range(len(s)+1)]
        wordDict = set(wordDict)

        return self.recursive(s, wordDict, dp, 0)
    
    def recursive(self, s, wordDict, dp, i):
        if i == len(s): return True
        if dp[i] != -1: return dp[i]

        for k in range(i, len(s)):
            if s[i:k+1] in wordDict:
                if self.recursive(s, wordDict, dp, k+1):
                    dp[k+1] = True
                else:
                    dp[k+1] = False
        return dp[len(s)] == True
    
    