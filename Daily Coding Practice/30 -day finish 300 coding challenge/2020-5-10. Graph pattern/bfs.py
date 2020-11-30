def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    # Write - Your - Code
    visited = [[False] for i in range(g.vertices)]
    
    queue = collections.deque()
    queue.append(source)
    while queue:
        max_len = len(queue)
        for i in range(max_len):
            neighbor = queue.popleft()
            print(neighbor, '///')
            result += str(neighbor)
            temp = g.array[neighbor].head_node
            while temp:
                if not visited[temp.data]:
                    queue.append(temp.data)
                    visited[temp.data] = True
                temp = temp.next_element
    # For the above graph, it should return "01234" or "02143" etc
    return result