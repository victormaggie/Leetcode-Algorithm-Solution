// implement next permutation, which rearrange numbers into the lexicographically next greater permuation

var nextPermutation = function(nums) {

    let n = nums.length-1;

    // find the next value

    while (n -1 >= 0 && nums[n -1] > nums[n]) {
        n --;
    }

    // find the larger value here 
    k = n - 1
    
    swap_index = k;
    while (nums[swap_index] < nums[swap_index-1]) {
        swap_index --;
    }
    swap_index --;

    // swap here 
    [nums[k], nums[swap_index]] = [nums[swap_index], nums[k]];

    // move to the end;
    let l = k + 1, r = nums.length-1;
    while (l < r) {
        [nums[l], nums[r]] = [nums[r], nums[l]];
        l ++;
        r --;
    }
}