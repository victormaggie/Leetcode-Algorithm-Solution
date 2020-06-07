class Solution:
    # this is a very practical problem
    # it is very practical problem where the it is should be used to random sampling

    def __init__(self, w: List[int]):
        """
        :type: w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
    
    # with binary search

    def pickIndex(self) -> int:
        target = self.prefix_sums * random.random()
        low, high = 0, len(self.prefix_sums)
        for i, prefix_sum in enumerate(self.prefix_sums):
            mid = low + (high - low) //2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
