var moveZeros = function(nums) {
    let j = 0;
    for (let i = 0; i < nums.length; i++) {
        // swap here
        var b = nums[i];
        nums[i] = nums[j];
        nums[j] = b;
        j += 1;
    }
};