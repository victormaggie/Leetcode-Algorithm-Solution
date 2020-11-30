var permuteUnique = function(nums) {
    
    nums.sort((a, b) => a-b)
    let visited = Array(nums.length).fill(1);
    let res = []
    dfs(nums, res, visited, []);
    return res;
    
    function dfs(nums,  res, visited, path) {
        if (path.length == nums.length) {
            res.push(path.slice());
            return;
        }
        
        for (let i = 0; i < nums.length; i++) {
            
            if (visited[i] === 0) continue;
            if (i && nums[i] === nums[i-1] && visited[i-1] === 0) continue;
            
            visited[i] = 0;
            path.push(nums[i]);
            dfs(nums, res, visited, path);
            visited[i] = 1;
            path.pop();
        }
    }
};
// backtracking