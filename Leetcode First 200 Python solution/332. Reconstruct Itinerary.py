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
            # The memorize the visited one
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
                # backtracking to get all the possible solution
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                
                if ret:
                    return True
            
        return False

# Time complexity : o(d ^ |E|)   --> d ^ |E|      we have |E| airport, each airport has d possible flight choice , so d ^ |E| 
# Space complexity o(|E| + |V|}) -> The recursion would be exactly the number of flights in the input extra o(|E|)  -> Total space complexity o(2|E| + |v|)


class Solution:

    def findItinerary(self, tickets):
        
        # define the travelling graph
        graph = {}
        
        for depart, destination in tickets:
            
            if not graph.get(depart): graph[depart] = []
            graph[depart].append(destination)
        
        # sort the lexical destination
        
        for depart, destination in graph.items():
            destination.sort()
        
        ans = []
        
        # use the Euler path o(|E|)
        def dfs(start):
            dest_List = graph.get(start)
            while dest_List:
                new_start = dest_List.pop(0)
                dfs(new_start)
            ans.append(start)
        
        dfs('JFK')
        return ans[::-1]
        

# Time complexity o(|E|log(|E|/|v|))
# Space complexity o(|E| + |V|)  + o(|E|) traversal

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

