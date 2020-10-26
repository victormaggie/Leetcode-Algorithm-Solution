var removeDuplicates = function(nums) {

    let k = 0;
    for (let i = 0; i < nums.length; i++) {
        if (!i || nums[i] != nums[i-1]){
            nums[k++] = nums[i];
        }
    }
    return k;
};

// o(n) solution

