class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        
        stack = []
        for i in nums1:
            if i in nums2:
                stack.append(i)
                nums2.remove(i)
        return stack

# time complexity o(n+m)
# space complexity o(n+m)

# use hash table solution

    def intersect1(self, nums1, nums2):
        if len(nums2) > len(nums1):
            return self.intersect1(nums2, nums1)
        
        stack = []
        for i in nums1:
            if i in nums2:
                stack.append(i)
                nums2.remove(i)
        return stack
    
    def intersect2(self, nums1, nums2):
        import collections
        if len(nums2) > len(nums1):
            return self.intersect2(nums2, nums1)
        
        stack = []
        hash_table = collections.defaultdict(int)
        for i in nums1:
            hash_table[i] += 1 if i in hash_table else 0
        
        for i in nums2:
            if i in nums2 and hash_table[i] >0:
                hash_table[i] -= 1
                stack.append(i)

        return stack



        