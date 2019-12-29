class Solution(object):
    def intersection(self, nums1, nums2):
        import numpy as np 
        nums1 = np.unique(nums1)
        nums2 = np.unique(nums2)
        stack = []

        if len(nums1) > len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    stack.append(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    stack.append(nums2[i])
        return stack

# time complexity o(n x m)
# space complexity o(n+m)
# optimization for the solution lol

    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        # iterate, num = [i, num for (i, num) in max((len(nums1), nums1), (len(nums2), nums2))]
        if len(nums1) > len(nums2):
            pass
        else:
            nums1, nums2 = nums2, nums1                     
        stack = [i for i in nums1 if i in nums2]
        return stack

        #  not conversion --> 
    def intersection3(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        return [i for i in nums1 if i in nums2]

# time complexity: o(n+m)  --> contain/ in in o(1)
# space complexity: o(n+m) --> new stack
    def intersection4(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)

# time complexity o(m+n)
# time complexity o(m+n)

