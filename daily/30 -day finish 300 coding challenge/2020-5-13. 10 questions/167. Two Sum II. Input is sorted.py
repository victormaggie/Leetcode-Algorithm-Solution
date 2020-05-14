class Solution:
    def twoSum(self, numbers, target):
        hashmap = {}
        for i in range(len(numbers)):
            if numbers[i] in hashmap:
                return [hashmap[numbers[i]] + 1, i + 1]
            key = target - numbers[i]
            hashmap[key] = i

# time complexity o(n)
# space complexity o(n)
