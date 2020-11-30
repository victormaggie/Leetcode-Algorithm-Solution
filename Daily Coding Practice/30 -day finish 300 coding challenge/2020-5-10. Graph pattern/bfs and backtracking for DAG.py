# this is very helpful algorithms 
# combine the bfs and backtracking
class Solution:
    def Topological_sort_all_path(self, tasks, prerequisites):
        if tasks <= 0: return False
        import collections
        result = []
        #a. Initialization of the Graph and inDegree order
        Graph = {i: [] for i in range(tasks)}
        inDegree = {i: 0 for i in range(tasks)}
        queue = collections.deque()

        #b. Generate the Graph and inDegree order
        for parent, child in prerequisites:
            Graph[parent].append(child)
            inDegree[child] += 1
        
        #c. Find the source algorithm
        for i in inDegree:
            if inDegree[i] == 0:
                queue.append(i)

        #d. Use backtracking to get all the results
        return back_tracking(self, Graph, queue, inDegree, result)
    
    def back_tracking(self, Graph, queue, inDegree, result):
        if queue:
            for vertext in queue:
                copyofqueue = queue
                result.append(vertext)
                copyofqueue.remove(vertext)
                # update the inDegree
                # additional o(E) --> move and add back
                for child in Graph[vertext]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        copyofqueue.append(child)
                
                # recursion for the calculation
                self.back_tracking(Graph, queue, inDegree, result)

                # recover the previous condition of result list and inDegree
                result.pop()
                for child in Graph[vertext]:
                    inDegree[child] += 1
        
        if len(result) == len(inDegree):
            return result
    
    
# This is a great solution
# time complexity o(v! * E)  V is the total number of tasks and E is the number of total prerequisites




