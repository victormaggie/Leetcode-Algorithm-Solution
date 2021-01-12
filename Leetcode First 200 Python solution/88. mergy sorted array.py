
class Solution:
    def merge(self, nums1, m, nums2, n):
        
        tot = m + n + 1
        
        n = n - 1
        m = m - 1
        
        while m >= 0 and n >= 0:
            
            if nums1[m] > nums2[n]:
                nums1[tot] = nums1[m]
                m -= 1
            else:
                nums1[tot] = nums2[n]
                n -= 1
            tot -= 1
        
        nums1[:n+1] = nums2[:n+1]

# o(n) solution
