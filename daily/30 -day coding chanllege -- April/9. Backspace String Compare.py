class Solution:
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for i in reversed(S):
                if i == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield i
        return all(s == t for s, t in itertools.zip_longest(F(S), F(T)))

# time complexity o(n)
# space complexity o(1)