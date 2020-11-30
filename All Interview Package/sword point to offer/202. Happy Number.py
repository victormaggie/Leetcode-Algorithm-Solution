class Solution:

    def isHappy(self, n):

        def cal_func(n):
            return sum(map(lambda x: int(x)**2, str(n)))

        slow, fast = n, cal_func(n)

        while slow != fast and fast != 1:
            slow = cal_func(slow)
            fast = cal_func(cal_func(fast))
        
        return fast == 1 or not fast == fast

# space complextity o(1)


    def isHappy(self, n):
        
        visited = set()
        visited.add(n)

        while True:
            temp = 0

            while n:
                digit = n % 10
                temp += digit **2
                n //= 10
            
            if temp == 1: return True
            if temp in visited: return False
            visited.add(temp)
            n = temp

# space complexity o(n)
