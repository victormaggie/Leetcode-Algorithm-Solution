class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return
        if len(matrix) == 1: return matrix[0]
        # define boundary 

        ## another version is the string type
        T, L, B, R = 0, 0, len(matrix)-1, len(matrix[0])-1
        stack = []
        direction = 0
        while T <= B and L <= R:
            if direction == 0:
                for j in range(L, R+1):
                    stack.append(matrix[T][j])
                T += 1
                direction = 1
            
            elif direction == 1:
                for i in range(T, B+1):
                    stack.append(matrix[i][R])
                R -= 1
                direction = 2
            
            elif direction == 2:
                for j in range(R, L-1, -1):
                    stack.append(matrix[B][j])
                B -= 1
                direction = 3
            
            elif direction == 3:
                for i in range(B, T-1, -1):
                    stack.append(matrix[i][L])
            
                L += 1
                direction = 0

        return stack

# version 3

