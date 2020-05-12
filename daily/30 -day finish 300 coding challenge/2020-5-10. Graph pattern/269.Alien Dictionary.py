class Solution:
    # this is a really difficult question
    # topological sort
    def alienOrder(self, words):
        if len(words) == 0: return ''

        # a. Initialize the Graph and inDegree
        inDegree = {}
        Graph = {}
        for word in words:
            for character in word:
                inDegree[character] = 0
                Graph[character] = []

        # b. Build the Graph and inDegree
        for i in words:
            w1, w2 = words[i], words[i+1]
            for j in range(0, min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]
                if parent != child:
                    Graph[parent].append(child)
                    inDegree[child]+=1
            else:
                if len(w2) < len(w1): return ''
        
        # c. Find the source for the calculation
        source = collections.deque()
        while source:
            vertext = source.popleft()
            res.append(vertext)
            for child in Graph[vertext]
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    source.append(child)
        
        if len(res) < len(inDegree):
            return ''
        return ''.join(res)
    
# time complexity o(v+e)
# space complexity o(v+e)
                

