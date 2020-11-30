class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix[0]) == 0:
            return False
        import functools
        List = functools.reduce(lambda x, y: x+y, matrix)

        left, right = 0, len(List) -1

        while left <= right:
            mid = (left + right) //2
            if List[mid] == target:
                return True
            elif List[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return False

