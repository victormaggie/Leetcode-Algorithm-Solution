
var findDuplicates = function(nums) {
    
    let ans = [];


    for (let num of nums) {
        if (nums[Math.abs(num)-1] < 0) {
            ans.push(Math.abs(num));
        }
        nums[Math.abs(num)-1] *= -1;
    }
    
    return ans;
    
};

// o(n)
