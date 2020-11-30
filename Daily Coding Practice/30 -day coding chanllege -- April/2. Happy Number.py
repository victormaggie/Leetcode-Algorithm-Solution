# Happy number 
# be aware of that the duplicate number is not at the first one
# need an array to store the sorted number

class Solution:
    def isHappy(self, n):
        seen = []
        while True:
            n_sum = 0
            while n:
                n_sum += (n % 10) ** 2
                n //= 10
            if n_sum in seen:
                return False
            seen.append(n_sum)
            if n_sum == 1:
                return True
            n = n_sum
