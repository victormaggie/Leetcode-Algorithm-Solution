# sqrt(x)
# we use the binary search method for this
class Solutions(object):

    def mySqrt(self, x):
        l, r = 0, x + 1
        # [left, right)

        while l < r:
            mid = (l+r)//2
            if mid**2 == x:
                return mid
            
            if ( mid**2 <= x):     # mid is large than ans
                l = mid
            else:
                r = mid - 1

        return r

class Solutions2(object):

    def mySqrt(self, x):

        num = x
        while num * num > x:
            num = (num + x/num)/2
        return num



