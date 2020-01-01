class solution(object):
    def subarraySum(self, nums, k):
        """
        Brute force solution
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for index in range(i, j+1):
                    sum += nums[index]
                if sum == k:
                    count += 1
        
        return count

# time complexity o(n^3)
# space complexity o(1)
    
    def subarraySum3(self, nums, k):
        import collections
        count = 0
        # prefix subarray
        # prefixSum[x] = prefixSum[x-1] + nums[x]
        hash_map = collections.defaultdict(int)
        hash_map[0] = 1
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if sum - k in prefixSum:
                count += hash_map[sum-k]
            hash_map[prefixSum] += 1
        return count 



            
