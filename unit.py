import unittest
import logging
from ddt import ddt, data, unpack

@ddt
class Solution(unittest.TestCase):
	# bucket sort solution
    
    def sortColors(self, nums):
        self.assertNotEqual(nums, [])
        hash = {i : [] for i in range(3)}
        [hash[i].append(i) for i in nums]
        
        index = 0
        for i in hash:
            for j in hash[i]:
                nums[index] = j
                index += 1
        return nums
    
    def fibonacci_iter(self, n):
        f_0 = 0
        f_1 = 1
        
        if n < 2: return n
        for i in range(n-1):
            f_0, f_1 = f_1, f_1 + f_0
        
        return f_1
    
    def memo(function):
        cache = {}
        
        def decorated_function(*args):
            if args in cache:
                return cache[args]
            else:
                val = function(*args)
                cache[args] = val
                return val
        return decorated_function
    
    @memo
    def fibonacci_recursion(self, n):
        if n < 2: return n
        
        return self.fibonacci_recursion(n-1) + self.fibonacci_recursion(n-2)
        
    def fibonacci_memo(self, n):
        
        if n < 2: return n
        memo = [0] * (n+1) 
        memo[0] = 0
        memo[1] = 1
        
        def fibo_memo(n):
            if n < 2: return n
            if memo[n]: return memo[n]
            memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
            return memo[n]
        
        return fibo_memo(n)
    
    #@data([[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]], [[2, 0, 1], [0, 1, 2]])
    @data([2, 0, 2, 1, 1, 0], [2, 0, 1])
    def test_1(self, nums):
        self.sortColors(nums)
        
    @data([3], [4])
    @unpack
    def test_2(self, nums):
        self.fibonacci_iter(nums)
        
    @data([3], [4])
    @unpack
    def test_3(self, nums):
        print(self.fibonacci_recursion(nums), '...sss')
        
    @data([3], [5])
    @unpack
    def test_4(self, nums):
        print(self.fibonacci_memo(nums))
        
if __name__ == "__main__":
    unittest.main()
    
    