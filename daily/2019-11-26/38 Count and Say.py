class Solution:
    def countAndSay(self, n):

        s = '1'
        for i in range(1, n):

            curr_s = ''
            j = 0
            while j < len(s):
                u = j
                # count how many same 1 or 2
                while u < len(s) and s[u] == s[j]:
                    u += 1
                curr_s += str(u-j)
                curr_s += s[j]

                # update the j
                j = u
            
            s = curr_s
        
        return s