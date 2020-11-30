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

    def findLengthOfCIS2(self, nums: List[int]) -> int:
        idx, ans = 0, 0

        while idx < len(nums):
            count = 1
            while idx + 1 < len(nums) and nums[idx+1] > nums[idx]:
                count, idx = count + 1, idx + 1
            ans = max(count, ans)
            idx += 1
        return ans
# time complexity o(n)
# space complexity o(1)



if __name__ == "__main__":
    nums = [4,5,6,2,1,4]
    test = Solution()
    print(test.findLengthOfCIS2(nums))

