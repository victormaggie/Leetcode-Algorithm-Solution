var canJump = function(nums) {
    
    // track the step
    // memorize the how far it can go

    for (let i = 0, memo = 0; i < nums.length; i++) {
        if (i > memo) return false;
        memo = Math.max(nums[i] + i, memo)
    }
    return true;
};

// o(n) greedy