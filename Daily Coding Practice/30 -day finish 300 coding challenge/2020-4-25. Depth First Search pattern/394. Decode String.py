class Solution:
    def decodeString(self, s):
        stack = []
        curstring = ''
        cur_num = 0
        for char in s:
            if char.isnumeric():
                cur_num = cur_num  * 10 + int(char)
            elif char == "[":
                stack.append(curstring)
                stack.append(cur_num)
                curstring = ''
                cur_num = 0
            elif char == "]":
                num = stack.pop()
                prestring = stack.pop()
                curstring = prestring + num * curstring
            else:
                curstring += char
        return curstring

# time complexity o(N)
# space complexity o(N)

########## how to solve this problem use the DFS >?????????