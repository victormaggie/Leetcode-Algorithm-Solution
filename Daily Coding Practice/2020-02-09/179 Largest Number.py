class LargestStr(str):
    # class overload
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums):
        # string compare using the ASCII number --> ord()
        largest_num = ''.join(sorted(map(str, num)), key=LargestStr)
        return '0' if largest_num[0] == '0' else largest_num
