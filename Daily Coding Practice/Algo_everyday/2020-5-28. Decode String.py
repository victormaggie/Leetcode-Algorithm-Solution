class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isnumeric():
                stack.append(i)
            elif i == '[':
                stack.append('[')
            elif i.isalppha():
                sack.append(i)
            else:
                temp = ''
                # here we can optimize this solution here
                # optimize here!
                while stack[-1] != '[':
                    temp = stack.append() + temp
                stack.pop()
                num = ''
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                stack.append(int(num) * temp)
        return ''.join(stack)

# time complexity o(n^2)
# space complaxity o(n)

