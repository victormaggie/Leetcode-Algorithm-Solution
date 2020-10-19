class Solution:
    def bestTeamScore(self, scores, ages):
        if len(scores) == 0 or len(ages) == 0: return 0

        array = []
        for a, b in zip(ages, scores):
            array.append((a, b))
        q = sorted(array, key = lambda x: (x[0], x[1]), revrese=True)
        f = [0] * len(q)
        res = 0
        for i in range(0, len(q)):
            score = q[i][1]
            f[i] = score
            for j in range(0, i):
                if q[j][1] >= q[i][1]:
                    f[i] = max(f[i], f[j] + score)
            
            res = max(res, f[i])

        return res

# o(n ^ 2) solution here!
