class Solution:
    def minWindow(self, s, t):
        # edge case
        if len(s) < len(t): return ''
        startwin, substr_start, matched = 0, 0, 0
        win_size = float('inf')
        char_frequency = collections.defaultdict(int)

        for i in t: char_frequency[i] += 1

        for endwin in range(len(s)):
            if s[endwin] in char_frequency:
                char_frequency[s[endwin]] -= 1
                if char_frequency[s[endwin]] >= 0:
                    matched += 1
            
            while matched == len(t):
                # check the smallest window
                if win_size >= endwin - startwin + 1:
                    win_size = endwin - startwin + 1
                    substr_start = startwin
                
                left_char = s[startwin]
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1
                startwin += 1
        
        if win_size == float('inf'): return ''
        return s[substr_start:substr_start+win_size]

# time complexity o(n+m)
# space complxity o(n)

