class Solution:
    def isHappy(self, n):
        seen = []
        # seen = set()
        # the hashset lookup o(1)
        while True:
            seen.append(n)
            # seen.add(n)
            res = 0
            while n:
                res = (n % 10) ** 2 + res
                n = n // 10
            if res == 1: return True
            if res in seen: break
            n = res
        return False

# time complexity o(logn)
# space complexity o(n)