# This is a very good solution for the moving window 
# Be aware of that, the permutation has no order
# use the hashtable and moving window to solve this question

class Solution:
    def checkInclusion(self, s1, s2):
        hashtable = collections.defaultdict(int)
        wins = collections.defaultdict(int)

        for i in s1: hashtable[i] == 1

        k = len(s1)
        for i in range(len(s2)):
            if i < k:
                wins[s2[i]] += 1
            else:
                wins[s2[i-k]] -= 1
                if wins[s2[i-k]] == 0: del wins[s2[i-k]]
                wins[s2[i]] += 1
            
            if wins == hashtable: return True
        
        return False

# time complexity o(N)
# space complexity o(26  *2 ) = o(1)