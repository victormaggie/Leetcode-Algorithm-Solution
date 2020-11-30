# Solution 1 (this solution we can know left and right)
class Solution:
    def minAddToMakeValid(self, S:str) -> int:
        right = left = 0
        for i in S:
            if right == 0 and i == ")":
                left += 1

            else:
                right += 1 if i == "(" else -1
        return right + left


# Solution 2 (the stack solution count the number)

    def minAddToMakeValid(self, S:str) -> int:
        stack = []
        for i in S:
            if i == "(":
                stack.append(i)
            else:
                if stack == []:
                    stack.append(i)
                else:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(i)
        return len(stack)

