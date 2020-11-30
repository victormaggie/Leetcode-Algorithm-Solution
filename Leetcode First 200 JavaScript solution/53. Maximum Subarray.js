var maxSubArray = function(nums) {
    if (nums.length == 0) return 0;
    let Sum = 0;
    let ans = -0X7FFFFFFF;

    for (let i = 0; i < nums.length; i++) {
        Sum += sums[i];
        Sum = Math.max(Sum, nums[i]);
        ans = Math.max(Sum, ans);
    }
    return ans;
}

// o (n) greedy solution
