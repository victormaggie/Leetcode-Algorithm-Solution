class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # hashmap 
        # hashset 
        # monotonic stack

        count = collections.Counter(s)
        stack = []
        seen = set()

        for i in s:
            if i in seen:
                count[i] -= 1
            
            else:
                while stack and stack[-1] > i and count[stack[-1]] > 0:
                    seen.remove(stack[-1])
                    stack.pop()
                
                count[i] -= 1
                stack.append(i)
                seen.add(i)
        return ''.join(stack)

# o(n) time complexity
# space complexity o(n)