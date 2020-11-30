# naive solution 
# cannot pass time limit
class solution:
    def subarray(self, k):
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) == k:
                    res += 1
        return res

# time complexity o(n^3)
# space complexity o(1)

# prefixsum solution
class solution:
    def subarray(self, k):
        res = 0
        for i in range(len(nums)):
            prefixsum = 0
            for j in range(i, len(nums)):
                prefixsum += nums[i]
                if prefixsum == k:
                    res += 1
                elif prefixsum > k:
                    continue
        return res

# time complexity (o(n^2))
# space complexity o(1)

# prefixsum array solution
class solution:
    def subarraysum(self, nums, k):
        count = 0
        prefix = 0
        prefixSum = collections.defaultdict(int)
        sum = 0
        for i in range(len(nums)):
            sum += sum[i]
            if sum-k in prefixhash_map:
                count += prefixSum[sum-k]
            
            prefixSum[sum] += 1
        return count

# time complexity o(n)
# space complexity o(n)

class solution:
    def subarraySum(self, nums, k):
        count, cur, res = {0:1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur-k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res

# time complexity o(n)
# space complexity o(n)

# 2020-4-22