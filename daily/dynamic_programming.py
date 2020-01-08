class dynamic_programming(object): 

    
    # dynamic programming
    # 1. stack
    # 2. Initializaiton
    # 3. Transition
    # 4. Res
    def climbStairs(self,n):
        # define stack
        stack = [0] * (n+1)
        # initialization
        stack[0] = 1
        stack[1] = 1

        for i in range(2, n+1):
            # transition matrix
            stack[i] = stack[i-1] + stack[i-2]
        # result
        return stack[-1]

    def trap_water(self, array):

        # edge case
        if not array: return 0

        # left hightest point
        left = []
        # right hightest point
        right = []

        # initialization the matrix
        left[0] = array[0]
        # initialization the matrix
        right[0] = array[-1]

        # Transition matrix

        for i in range(1, len(array)):
            left[i] = max(left[i-1], array[i])
        for j in range(len(array)-2, -1, -1):
            right[i] = max(right[i+1], array[i])
        
        sum = 0
        for i in range(1, len(array)-1):
            value = min(left[i], right[i]) - array[i]
            sum += value if value > 0 else 0
        return sum

