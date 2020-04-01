############################################## Q1 ######################################
# Find Lucky Interger in an Array
class Solution:
    def findLucky(self, arr):
        hash_table = dict(collections.Counter(arr))
        for key in sorted(hash_table.keys(), reverse=True):
            if key == hash_table[key]:
                return key
        return -1

# time complexity o(n) + o(m) + o(nlogn)
# space complexity o(1)
class Solution:
    def findLucky(self, arr):
        hash_table = dict(collections.Counter(arr))
        for key in sorted(hash_table, reverse=True):
            if key == hash_table[key]:
                return key
        return -1

# time complexity is the same

class Solution:
    def findLucky(self, arr):
        return max([key for key, val in collections.Counter(arr) if key == val], default=-1)

        # time complexity o(n) + o(m)  without sorted
        # space complexity o(n)

####################################### Q2 1395 Count Number of Teams #############################

# be aware of the scope of the number n < 200, that means the o(n^3) can pass the calculation
# brute force solution!


class Solution:
    def numTeams(self, rating):
        res = []
        return self.montonic(rating) + self.montonic(rating[::-1])
    
    def montonic(self, rating):
        res = []
        for i in range(len(rating)):
            temp = []
            temp.append(rating[i])
            for j in range(i, len(rating)):
                if rating[j] > rating[i]:
                    temp.append(rating[j])
                    for k in range(j, len(rating)):
                        temp.append(rating[k])
                        res.append(temp[:])
                        temp.pop()
                        continue
                    temp.pop()
                    continue
            temp.pop()
            continue
        return len(res)

# This can return all the list
# time complexity o(n^3)
# space compleixty o(n)
# ---------> 1440 ms

# Optimization of the algorithm
class Solution:
    def numTeams(self, rating):
        res = 0
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    # calculation the increasing or decreasing
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        res += 1
        return res

# time complexity o(n^3)
# space complexity o(1)
# -----> 1200 ms 

# further Optimization of the algorithm

class Solution:
    def numTeams(self, rating):
        n = len(rating)
        res = 0
        for i in range(n):
            left = 0
            right = 0
            for j in range(i):
                if rating[j] < rating[i]: left += 1
            for k in range(i+1, n):
                if rating[k] > rating[i]: right += 1
            res += (left * right + (i-left) * (n-1-right-i))
        return res

# time complexity o(n^2)
# space complexity o(1)
# -------> 52 ms

############################################## Q 3. Design Underground System ######################

# use the hash map data structure 

class UndergroundSystem:
    def __init__(self):
        # define hash_map
        self.user = collections.defaultdict(list)
        self.dest = collections.defaultdict(list)
    
    def checkIn(self, id, stationName, t):
        self.user[id] = [stationName, t]
    
    def checkOut(self, id, stationName, t):
        startStation, prev_time = self.user[id]
        self.dest[(start_station, stationName)].append(t-prev_time)
    
    def getAverageTime(self, startStation, endStation):
        return float(sum(self.des[(startStation, endStation)]))/ len(self.dest[startStation, endStation])



