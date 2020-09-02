var findOrder = function(numCourses, prerequisites){
    const graph = new Map();
    const indegree = Array(numCourse).fill(0);
    const queue = [];
    const ans = [];

    // build the graph
    for (const [child, parent] of prerequisites) {
        if (graph.has(parent)) {
            graph.get(parent).push(child);
        } else {
            graph.set(parent, [child])
        }
        indegree[child]++;
    }

    // find the source here
    for (let i = 0; i < indegree.length; i++) {
        if (indegree[i] === 0) queue.push(i)
    }

    while (queue.length) {
        parent = queue.shift();
        if (graph.get(parent)) {
            for (const child in graph.get(node)) {
                if (indegree[child] === 0) queue.push(child);
            }
        }
    }
    if (ans.length = numCourses) return ans;
    return [];
};