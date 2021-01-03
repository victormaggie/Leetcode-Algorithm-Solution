
# string permutation by changing case

"""
"ad52"
"Ad52"

"""

class Solution:
    def letterCasePermutation(self, S):
    
        # use recursion method
        
        temp = []
        ans = []
        
        def dfs(S, ans, temp, idx):
            if len(S) == len(temp):
                ans.append(temp)
                return
            
            if S[idx].isalpha():
                dfs(S, ans, temp+S[idx].upper(), idx+1)
                dfs(S, ans, temp+S[idx].lower(), idx+1)
            
            else:
                dfs(S, ans, temp+S[idx], idx+1)
        
        dfs(S, ans, '', 0)
        return ans


        
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        # recursive solution
        
        ans = ['']
        
        for char in S:
            n = len(ans)
            #o(N)
            if char.isalpha():
                for i in range(n):
                    # o(2 ^ N)
                    ans.append(ans[i])
                    ans[i] += char.lower()
                    ans[n+i]+= char.upper()
            else:
                
                for i in range(n):
                    ans[i] += char
        
        return ans

# the iterate solution is better !   
# time complexity o(n * 2^n) 
