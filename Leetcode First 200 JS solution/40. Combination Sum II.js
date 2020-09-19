var combinationSum2 = function(candidates, target) {
    let ans = [], temp = [];

    if (!candidates || !candidates[0]) return [[]];
    candidates.sort((a, b) => a-b);
    combinationSum2(candidates, temp, target, ans, 0);
    return ans;

    function combination(candidates, temp, target, ans, idx) {
        if (target == 0) {
            ans.push(temp.slice());
            return
        }

        for (let i=idx; i < candidates.length; i++) {
            if (candidates[i] > target) break;
            if (i != idx && candidates[i] === candidates[i-1]) continue;
            temp.push(candidates[i])
            combination(candidates, temp, target-candidates[i], ans, i+1);
            temp.pop();
        }
    }
}

// o(2^n)
// o(n)