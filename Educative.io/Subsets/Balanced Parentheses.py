
# Balanced Parenthese (Hard)

"""
Given a number "N", write a function to generate all combination of 'N', pairs of balanced parenthese

"""


def generate_valid_parenthese(num):
    
    result = []
    
    def dfs(left, right, path, result):
        
        if left == 0 and right == 0:
            result.append(path)
            return 
        
        if left > 0:
            dfs(left-1, right, path+'(', result)
        
        if right > left:
            dfs(left, right-1, path + ')', result)
    
    dfs(num, num, '', result)
    return result