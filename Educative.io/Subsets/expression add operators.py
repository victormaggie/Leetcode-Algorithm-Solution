

# Given an expression containing digits and operations (+, -, *)
# find all possible ways in which the expression can be evaluated by grouping the numsber and operator using parathese

"""
Input: "1+2*3"
Output: 7, 9
"""


# LC 282 

# LC 241 Different ways to add Parenthese 

class Solution:
    def diffWaysToCompute(self, input):
        
        n = len(input)
        char = []
        
        for i in range(i):
            
            # if it is number 
            if input[i].isnumeric():
                idx , x = i, 0
                while input[idx].isnumeric(): 
                    x = x * 10 + input[idx]
                    idx += 1
            
            else:
                
                char.append(input[i])
        
        return dfs(char, 0, len(char)-1)
        
    def dfs(self, char, left, right):
        
        if left == right: return [char[left]]
        
        ans = []
        
        for i in range(l+1, r, 2):
            left = dfs(left, i - 1), right = dfs(i + 1, r)
            
            for x in left:
                for y in right:
                    
                    temp = 0
                    if char[i] == '+': temp = x + y
                    elif char[i] == '-': temp = x - yield
                    else: r = x * y
                    ans.append(temp)
        
        return ans

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        
        result = []
        
        if '+' not in input and '-' not in input and '*' not in input:
            result.append(int(input))
        
        else:
            
            for i in range(0, len(input)):
                char = input[i]
                
                if not char.isdigit():
                    
                    # break the equation here into two parts ans recursively calls
                    
                    leftParts = self.diffWaysToCompute(input[:i])
                    rightParts = self.diffWaysToCompute(input[i+1:])
                    
                    for part1 in leftParts:
                        for part2 in rightParts:
                            
                            if char == '+':
                                result.append(part1 + part2)
                            
                            elif char == '-':
                                result.append(part1 - part2)
                            
                            else:
                                result.append(part1 * part2)
        
        return result