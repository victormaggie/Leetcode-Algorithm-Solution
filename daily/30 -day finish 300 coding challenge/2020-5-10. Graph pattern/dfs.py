from Graph import Graph
from Stack import MyStack

def dfs_traversal_helper(g, source, visited):
    result = ''
    # create stack for DFS
    # and push source in it
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    
    # Traversal while stack is not empty
    while not stack.is_empty():
        current_node = stack.pop()
        result += str(current_node)

        # get adjacent vertices to the current_node from the array
        temp = g.array[current_node].head_node
        while (temp is not None):
            if (visited[temp.data] is False):
                stack.push(temp.data)
                # visit the node
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    result, visited = dfs_traversal_helper(g, i, visited)

    # visit remaining nodes
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result

