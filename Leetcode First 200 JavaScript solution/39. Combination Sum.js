var combinationSum = function(nums, target) {

    nums.sort((a, b) => a - b);
    let res = [];

    dfs(nums, 0, target, []);
    return res;

    function dfs(nums, idx, target, path) {
        if (target === 0) {
            res.path(path.slice());
            return;
        }
        if (target < 0) {
            return;
        }
        for (let i = idx; i < nums.length; i++) {
            path.push(nums[i]);
            dfs(nums, i, target - nums[i], path);
            path.pop();
        }
    }
}

// 