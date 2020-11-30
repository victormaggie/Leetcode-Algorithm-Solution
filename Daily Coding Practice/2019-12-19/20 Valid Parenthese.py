class Solution:
    def isValid(self, s):
        # use hash map to solve this question
        # use the stack to store the data
        hash_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []

        # define a stack
        for i in s:
            if i not in hash_map:
                if stack and hash_map[stack.pop()] == i:
                    continue
                else:
                    return False
            else:
                stack.append(i)

        return stack == []


