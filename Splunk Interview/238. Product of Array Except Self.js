var productExceptSelf = function(nums) {

    stack = Array(nums.length).fill(1);

    // we first calculate the left accumulate 
    for (let i = 1; i < nums.length; i++) {
        stack[i] = nums[i-1] * stack[i-1]
    }

    // use this to calculat the right accumulate
    right = 1;
    // we calculate the right accumulation
    for (let i = nums.length-1; i >= 0; i--) {
        stack[i] *= right;
        right *= nums[i]
    }
    return stack;
}

// o(n) solution

