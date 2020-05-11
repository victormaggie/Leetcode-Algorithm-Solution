class Solution:
    def prisonAfterNDays(self, cells, N):
        prev_state = cells[:]
        ptr = 0
        count = 0
        while count < N:
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    prev_state[i] = 1
                else:
                    prev_state[i] = 0
            if count == 0:
                prev_state[0] = 0
                prev_state[-1] = 0
            count += 1
            cells = prev_state[:]
        return prev_state

# cannot pass the case for this brute force solution

class Solution:
    def prisonAfterNDays(self, cells, N):
        hashset = []
        count = 0
        for i in range(0, N):
            cells = self.nextday(cells)
            if cells in hashset:
                N %= count
                return hashset[N-1]
            hashset.append(cells)
            count += 1
        return cells
    
    def nextday(self, cells):
        return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in range(8)]

# time complexity  O(2N)
# space complexity o(N)


