class Solution:
    def sequenceReconstruction(self, org, seqs):
        # use the topographic sorting
        # if the queue has more than 1 source then break
        # check the final anwser

        # There is a typo, omg I debug for 1 hour

        if not seqs: return False

        # a. Initializae the graph and indegree
        Graph = {}
        inDegree = {}
        for sequence in seqs:
            for i in sequence:
                inDegree[i] = 0
                Graph[i] = []
        
        # b. Build the graph and indegree o(v+n)
        for sequence in seqs:
            for i in range(1, len(sequence)):
                parent, child = sequence[i-1], sequence[i]
                Graph[parent].append(child)
                inDegree[child] += 1
        
        if len(inDegree) != len(org): return False

        # c. Find the source of sequence
        source = collections.deque()
        for i in inDegree:
            if inDegree[i] == 0:
                source.append(i)
        
        # d. Topological sort for the calculation  o(v+e)
        res = []
        while source:
            max_len = len(soruce)
            if max_len > 1: return False
            if org[len(res)] != source[0]  # the next value is not the next org value
            vertext = source.popleft()
            res.append(vertext)
            for child in Graph[vertext]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    source.append(child)
        
        # e. return the final solution
        return len(res) == len(org)

# time complexity o(v + n)
# space complexity o(v+n)