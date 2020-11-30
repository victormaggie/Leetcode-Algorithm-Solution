def bfs_traversal_helper(g, source, visited):
    result = ""

    # create queue object
    # enqueue source in it
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True # Mark as visited
    while queue.is_empty() is False:
        current_node = queue.deque()
        result += str(current_node)
        # get adjacent vertices to the current_node from the list
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[current_node].head_node
        while temp is not None:
            if (visited[temp.data] is False):
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited


def bfs_traversal(g, source):
    result = ''
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        return result
    
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # add another memorization for the visited node
    # this is the only difference between the traversal a tree or a graph
    result, visited = bfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result

