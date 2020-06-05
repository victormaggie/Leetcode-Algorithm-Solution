class Solution:
    def twoCitySchedCost(self, costs: List[[List[int]]]) -> int:
        if not costs: return 
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
        return total
    
# Greedy algorithms:
# "Find minimum number of something to do something"
# "Find maximum number of something to fit in some conditions"

# The idea of greedy algorithm is to pick up the locally optimal move at each step
# that will lead to the globally optimal solution

