class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2: return []

        hashmap = collections.defaultdict(int)

        stack = []

        # monotonic stack

        for val in nums2:
            if not stack:
                stack.append(val)
                continue
            while stack and val > stack[-1]:
                key = stack.pop()
                hashmap[key] = val
            stack.append(val)

        for key in stack:
            hashmap[key] = -1
        
        res = []

        for key in nums1:
            val = hashmap.get(key, -1)
            res.append(val)
        
        return res

# o(n)
