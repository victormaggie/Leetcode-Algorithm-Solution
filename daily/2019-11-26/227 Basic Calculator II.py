class Solution:
    def calculate(self, s):
    # edge case
        if s == None:
            return
        num, stack, sign = 0, [], '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            
            if s[i] in '+-*/' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))

                num = 0
                sign = s[i]

        return sum(stack)
    
    # o(n)