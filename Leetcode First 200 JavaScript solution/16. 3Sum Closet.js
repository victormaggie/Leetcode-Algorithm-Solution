var threeSumClosest = function(nums, target) {
    
    let res = 0X7FFFFFF;
    nums.sort((a, b) => a - b)
    for (let i = 0; i < nums.length; i++) {
        if (i - 1 > 0 && nums[i] === nums[i-1]) continue;
        let left = i + 1, right = nums.length-1;
        
        while (left < right) {
            const totalSum = nums[i] + nums[left] + nums[right];
            if (Math.abs(totalSum - target) < Math.abs(target - res)){
                res = totalSum
            }
            if (totalSum > target) {
                right--;
            } else if (totalSum < target) {
                left++;
            } else {
                return target;
            }
        }
    }
    
    return res;
};

// 2Sum 3Sum 4Sum --> Same idea here -- > use two pointer

