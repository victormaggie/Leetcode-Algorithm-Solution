class Solution:
    def subarraySum(self, nums, k):
        count = 0
        # brute force solution
        for i in range(len(nums)):
            for j in range(0, i+1):
                if sum(nums[j:i+1]) == k:
                    count += 1
        return count

# brute force solution
# time complexity o(n^3)
# space complexity o(1)

    #### optimization for the calculation
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            temp = 0
            for j in range(0, i+1):
                temp += nums[j]
                if temp == k: count +=1
        return count

# time complexity o(n^2)
# space complexity o(1)


    ### optimization to o(n) time complexity  Hashmap
    ### prefixsum[i] - prefixsum[j] = k
    ### only need to use hash to restore the store the value and look up in the table
    ### Key: prefixsum    value: count
    
    # iterate all o(n), and look up the hash o(1)
    # break down into 0, 1,2,3,4 ...n    the front sum == k
    # break down into n+1, n+2 , ...m    the back  prefixsum[m] - prefixsum[n+1] == k
    def subarraySum(self, nums, k):
        hashmap = {0:1} # honestly we donot need to use this shit, just for simply code
        count = 0
        prefixsum = 0

        for v in nums:
            prefixsum += v
            count += hashmap.get(prefixsum-k, 0)
            hashmap[prefixsum] += hashmap.get(prefixsum,0) + 1
        return count

# time/space complexity o(N)
