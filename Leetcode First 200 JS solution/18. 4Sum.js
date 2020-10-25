var fourSum = function(nums, target) {
    
    let ans = [];
    nums.sort((a, b) => a-b)
    
    for (let i = 0; i < nums.length-3; i++) {
        if (i - 1 >= 0 && nums[i] === nums[i-1]) continue;
        for (let j = i+1; j < nums.length-2; j++) {
            if (j - 1 > i && nums[j] === nums[j-1]) continue;
            // two pointer solution here
            let left = j + 1, right = nums.length-1;
            while (left < right) {
                
                const totalSum = nums[i] + nums[j] + nums[left] + nums[right];
                
                if (totalSum > target) {
                    right --;
                } else if (totalSum < target) {
                    left ++;
                } else {
                    ans.push([nums[i], nums[j], nums[left], nums[right]]);
                    while (left < right && nums[right] == nums[right-1]) right--;
                    while (left < right && nums[left] === nums[left+1]) left++;
                    right--;
                    left++;
                }
            }
        }
    }
    return ans;
};


// o(n^3) solution here!!

