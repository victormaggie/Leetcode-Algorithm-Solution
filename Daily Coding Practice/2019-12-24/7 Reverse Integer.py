class Solution:
    def reverse(self, x):
        Flag = False
        if x < 0:
            Flag = True
        x = abs(x)
        res = 0
        while x:
            a = x % 10
            res = res * 10 + a
            x //= 10
            # stop earlier and check overflow
            if res > 2**31 -1 or x < -2**31:
                return 0
        if Flag:
            return -res
        return res

# time complexity o(logn)
# space complexity o(1)

    def reverse2(self, x):
        sign = -1 if x < 0 else 1
        # here int('0011') = 11
        # no need to worry about it
        r = int(str(abs(x))[::-1])
        return (sign * r, 0)[r > 2**31 - 1]




