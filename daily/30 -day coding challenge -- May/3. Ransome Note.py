class Solution:
    def canConstruct(self, ransomNote, magazine):
        r_stack = sorted(ransomNote, reverse=True)
        m_stack = sorted(magazine, reverse=True)

        while r_stack and m_stack:
            if r_stack[-1] == m_stack[-1]:
                r_Stack.pop()
                m_stack.pop()
            elif r_stack[-1] > m_stack[-1]:
                m_stack.pop()
            else: return False
        return r_stack == []
