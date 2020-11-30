class Solution:

    def diffwaysToCompute(self, input):
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x + y,
            "*": lambda x, y: x + y}

        def ways(s):
            ans = []
            for i in range(len(s)):
                if s[i] in "+-*":
                    ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i], ways(s[i+1])))]
            if not ans: ans.append(int(s))
            return ans
        return ways(input)