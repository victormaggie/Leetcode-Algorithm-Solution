def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item
    
# python version 3.3 or beyond

def flatten(L):
    for object in L:
        if hasattr(object, '__iter__') and not isinstance(object, str):
            yield from flatten(object)
        else:
            yield(object)

# cannot iterate flatten [1, 2, [2, 2, [3, 3]]]

def flatten(L):
    import functools
    X = functools.reduce(lambda x, y: x + y, L)
    return X

# cannot solve this problem [1, 2, [2, 2, [3, 3]]]

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # edge case
        if not matrix or not matrix[0]:
            return False
        if matrix[-1][-1] < target:
            return False
        if matrix[-1][-1] == target:
            return True
        row, column = len(matrix)-1, len(matrix[0])-1    
        up, down = 0, row
        left, right = 0, column
        
        search_row = -float('inf')
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][column] == target:
                return True
            
            elif matrix[mid][column] > target:
                up = mid + 1
            
            elif matrix[mid][column] < target:
                down = mid - 1
            
            if matrix[mid][column] > target and (matrix[mid-1][column] < target or mid - 1 <0 ):
                search_row = mid
                break
        
        return self.binary_search(matrix, search_row, target)
            
    def binary_search(self, matrix, row, target):
        left , right = 0, len(matrix[0])-1
        
        while left <= right:
            mid = (left + right)//2
            if matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid] > target:
                right = mid - 1
            
            elif matrix[row][mid] < target:
                left = mid + 1
        
        return False

# time complexity o(logn) + o(logm)
# space complexity o(1)

class Solution:
    def searchMatrix(self, matrix, target):
        # edge case
        if not matrix or not matrix[0]:
            return False
        if matrix[-1][-1] < target:
            return False
        if matrix[-1][-1] == target:
            return True
        
        m, n = len(matrix), len(matrix[0])

        # binary search part for this algorithm
        left, right = 0, m * n -1
        while left <= right:
            mid = left + (right - left)//2
            row = mid // n
            col = mid % n
            if matrix[row][col] > target:
                right = mid - 1
            
            elif matrix[row][col] < target:
                left = mid + 1
            
            else:
                return True
        return False

# time complexity o(logmn)
# space complexity o(1)

# we can decrease o(lognm) to o(logn) + o(logm)

