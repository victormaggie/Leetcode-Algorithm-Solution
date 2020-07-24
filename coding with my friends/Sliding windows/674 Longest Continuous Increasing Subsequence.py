from typing import List

class Solution:
    def findLengthOfCIS(self, nums: List[int]) -> int:
        front = 0
        end = 0
        stack = []
        res = 0

        for front in range(len(nums)):
            if not stack or stack[-1] < nums[front]:
                stack.append(nums[front])
                res = max(res, front - end + 1)
            else:
                while stack and stack[-1] >= nums[front]:
                    stack.pop(0)
                    end += 1
                stack.append(nums[front])
        return res

# time complexity o(n)
# space complexity o(n)

if __name__ == "__main__":
    nums = [4,5,6,2,1,4]
    test = Solution()
    print(test.findLengthOfCIS(nums))

