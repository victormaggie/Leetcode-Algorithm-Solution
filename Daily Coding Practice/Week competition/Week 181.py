# 1389 Create Target Array in the Given Order
class Solution:
    def createTargetArray(self, nums, index):
        res = []
        for idx, num in zip(index, nums):
            if res == []:
                res += [num]
            else:
                res = res[:idx] + [num] + res[idx:]
        return res
# time complexity o(m)
# space complexity o(n)
    def createTargetArray(self, nums, index):
        res = []
        for idx, num in zip(index, nums):
            res.insert(idx, num)
        return res

# time complexity o(n^2)
# space complexity o(n)


# 1390 Four divisors
class Solution:
    def sumFourDivisors(self, nums):
        res = 0
        for i in nums:
            curSum, curAns = 1 + nums[i], 2
            for j in range(2, int(sqrt(nums[i]))+1):
                if nums[i] % j == 0:
                # case 1: if can be divided only j
                    if nums[i] // j == j:
                        curSum += (nums[i] //j)
                        curAns += 1
                # case 2: if can be divided by 2
                    else:
                        curSum += (j + (nums[i] // j))
                        curAns += 2
            # brute force search
            if curAns == 4:
                res += curSum
        return res


# Check if there is a valid path

class Solution:
    def hasValidPath(self, grid):
        if not grid or not grid[0]:
            return 

        

    def valid_next(self, i,j):

        # up- down - right - left

        self.valid = {
            "r" : [1, 3, 5],
            "l"  : [1, 4, 6],
            "d" : [2, 5, 6]

        }

        self.street_dir ={
            1 : ['l', 'r'],
            2 : ['u', 'd'],
            3 : ['l', 'd'],
            4 : ['r', 'd'],
            5 : ['l', 'u'],
            6 : ['u', 'r']
        } 

        self.dirs = {
            'r' : [0, 1],
            'l' : [0, -1],
            'u' : [-1, 0],
            'd' : [1, 0]
        }