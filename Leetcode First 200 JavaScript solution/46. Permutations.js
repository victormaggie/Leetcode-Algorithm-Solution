var permute = function(nums) {
    let res = [];
    dfs (nums, []);
    return res;

    function dfs(nums, path) {
        if (path.length == nums.length) {
            res.push(path.slice());
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (path.includes(nums[i])) continue;
            path.push(nums[i]);
            dfs(nums, path);
            path.pop();
        }
    }
};

// use iteration to check the duplicate number
// this is pretty slow ! shit

var permutate = function(nums) {
    let res = [];
    let visited = Array(nums.length).fill(1);
    dfs(nums, visited, []);
    return res;

    function dfs(nums, visited, path){
        if (path.length === nums.length) {
            res.push(path.slice());
            return
        }

        for (let i = 0; i < nums.length; i++) {
            if (visited[i]){
                path.push(nums[i]);
                visited[i] = 0;
                dfs(nums, visited, path);
                visited[i] = 1;
                path.pop()
            }
        }
    }
}

// no need to be backtracking here

var permute = function(nums) {
    let ans = [];

    function dfs(nums, temp){
        if (temp.length === nums.length) ans.push(path);
        // iterate all the number
        for (let i = 0; i < nums.length; i++) {
            if (temp.includes(nums[i])) continue;
            dfs(nums, [...temp, nums[i]]);
        }
    }
    dfs(nums, []);
    return ans;
}
// N!