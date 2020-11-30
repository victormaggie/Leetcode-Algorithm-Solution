class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
# sort algorithm o(NlogN)
# space complexity o(N)

class Solution:
    def removeDuplicates(self, nums):
        # two pointer solution
        # nice solution !

        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = arr[j]
        return i + 1

# time complexity o(N)
# space complexity o(1)
