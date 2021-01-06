
## Count of Unique Binary Search Tree

class Solution:
    
    def count_trees(n):
        if n <= 1:
            return 1
            
        
        count = 0
        
        for i in range(1, n+1):
            
            left = count_trees(i-1)
            right = count_trees(n-i)
            
            count += (left * right)
            
        return count

