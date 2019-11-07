# play guess game
# pick a number from 1 to n. You have to guess which number I picked
# every time you guess wrong, i will tell you whether the number is higher or lower

# Binary search method
import random


random.seed(903474021)

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        left, right = 1, n

        while left <= right:
            mid = left + (right - left)//2
            t = self.guess(mid)
            if t == 0: return mid
            elif t == -1: right = mid
            elif t == 1: left = mid + 1

    def guess(self, mid):

        return -1