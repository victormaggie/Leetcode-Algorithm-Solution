class solution(object):
    def numSquares(self, n):
        import math
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        def min_NumSquares(k):
            # recursive solution

            if k in square_nums:
                return 1
            
            # define a min_num
            min_num = float('inf')
            for square in square_nums:
                if k < square:
                    break
                # update this level
                new_num = min_NumSquares(k-square) + 1
                min_num = min(new_num, min_num)
            return min_num
        return min_NumSquares(n)


# Dynamic programming

    def numSquares2(self, n):
        import math
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[-1]

