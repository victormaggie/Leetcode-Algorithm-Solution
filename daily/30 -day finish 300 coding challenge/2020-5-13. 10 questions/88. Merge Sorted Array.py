class Solution:
    def merge(self, nums1, m, nums2, n):
        p_nums1 = 0
        p_nums2 = 0
        p_total = m + n

        while p_nums1 < m and p_nums2 < n:
            if nums1[p_nums1] <= nums2[p_nums2]:
                p_nums1 += 1
            else:
                nums1[p_nums1], nums2[p_nums2] = nums2[p_nums2], nums1[p_nums1]
                p_nums1 += 1

                # we need swap the number
                # keep the nums1[0] smallest
                new_ptr = p_nums2
                while new_ptr + 1 < n and nums2[new_ptr] > nums2[new_ptr + 1]:
                    nums2[new_ptr], nums2[new_ptr + 1] = news2[new_ptr + 1], nums[new_ptr]
                    new_ptr += 1
        nums1[m: p_total] = nums2[:]

# time complexity o(N*N) worst case   --> not that good
# space complexity o(1)


class Solution:
    def merge(self, nums1, nums2):
        nums1[:] = sorted(nums1[:m] + nums2)

# time complexity o(nlogn)
# space complexity o(n)


class Solution:
    def merge(self, nums1, nums2):
        # two get pointers from num1 and nums2
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1  # the final lenght of the pointer

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        
        # add the missing element to the nums2
        nums1[:p2+1] = nums2[:p2+1]

# time complexity o(n)
# space complexity o(n)
# pretty smart solution, the question is a bit confusion