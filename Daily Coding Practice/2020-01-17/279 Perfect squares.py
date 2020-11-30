class Solution(object):
    def numSquares(self, n):
        
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                # stop condition
                if k < square:
                    break
                # recursion
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)

# the brute force solution will exceede the time

# dfs and divide
class Solution:
    def numSquares(self, n):
        square_nums = [ i **2 for i in range(1, int(math.sqrt(n)+1))]

        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level
                    
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder-square_num)
            queue = next_queue
        return level
