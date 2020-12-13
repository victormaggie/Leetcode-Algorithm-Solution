class Solution:

    def findItinerary(self, tickets):

        self.flightMap = defaultdict(list)
        
        # build the itinery map
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
        
        self.visitBitmap = {}
        
        # sort the itinerary based on lexical order
        for origin, itinerary in self.flightMap.items():
            itinerary.sort()
            self.visitBitmap[origin] = [False] * len(itinerary)
        
        self.flights = len(tickets)
        
        print(self.flights)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)
        
        return self.result
        
    def backtracking(self, origin, route):
        
        if len(route) == self.flights + 1:
            self.result = route
            return True
        
        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                
                if ret:
                    return True
            
        return False

# Time complexity : o(|E| ^ d)   --> |E| ^ d 
# Space complexity o(|E| + |V|}) -> The recursion would be exactly the number of flights in the input extra o(|E|)  -> Total space complexity o(2|E| + |v|)

