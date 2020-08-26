var missingElement = function(nums, k){
    let prev = nums[0];
    if (curr - prev - 1 >= k){
        return prev + k;
    } else{
        k -= (curr - prev - 1);
        prev = curr;
    }
    return nums.pop() + k;
}

// time complexity o(n)
// space complexity o(1)
