class Solution:
    def stringShift(s, shift):
        for i in shift:
            direction, num = i
            if direction == 0:
                # left shift
                s = s[num:] + s[:num]
            else:
                s = s[len(s)-num:] + s[:len(s)-num]
        return s
    
    # time complexityo(n + d)
    # space complexity o(n)

    