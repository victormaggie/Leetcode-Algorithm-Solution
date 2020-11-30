from collections import deque

## usage of the DAG : check the task schedule --> amazon package --> acylic check DAG

def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # b. Build the graph and inDegree Hashmap
    for edge in edges:
        parent, child = edge
        graph[parent].append(child)
        inDegree[child] += 1

    # c. Fina all sources all vertices with 0 in-degrees
    source = deque()
    for i in inDegree:
        if inDegree[i] == 0:
            source.append(i)
    
    # d. For each source, and it to the sortedOrder and substract one from all of its children's ind-degree
    while source:
        vertext = source.popleft()
        sortedOrder.append(vertext)
        for child in graph[vertext]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                source.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sortedOrder) != vertices:
        return []
    
    ## here we can use the algorithm to find the DAG print
    ## find the cyclic circle in the algorithm
    ## find the solution in the calculation
# time complexity o(v+e)
# space complexity o(v+e)

    

def print_orders(tasks, prerequisites):
    # TODO: Write your code here
    print()
    #a. Initialize the Graph and inDegree hashmap
    Graph = {i: [] for i in range(tasks)}
    inDegree = {i: 0 for i in range(tasks)}
    import collections
    queue = collections.deque()

    #b. Generate the adjacency list and inDegree hashmap
    for parent, child in prerequisites:
    Graph[parent].append(child)
    inDegree[child] += 1

    #c. Find the source node
    for i in inDegree:
    if inDegree[i] == 0:
        queue.append(i)
    res = []
    back_tracking(Graph, queue, inDegree, res)

import collections
def back_tracking(Graph, queue, inDegree, res):
    if queue:
    for vertext in queue:
        res.append(vertext)
        sourcefornextcall = collections.deque(queue)
        sourcefornextcall.remove(vertext)
        for i in Graph[vertext]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            sourcefornextcall.append(i)
        back_tracking(Graph, sourcefornextcall, inDegree, res)
        res.remove(i)
        for i in inDegree:
        inDegree[i] += 1
        
    if len(res) == tasks:
    print(res)



