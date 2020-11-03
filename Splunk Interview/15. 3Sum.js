var threeSum = function(nums) {
    
    let ans = [];
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length-2; i++) {
        if (i-1 >= 0 && nums[i] == nums[i-1]) continue;
        
        let left = i + 1, right = nums.length -1; target = -nums[i];
        if (nums[i] > 0) break;
        while (left < right) {
            
            if (nums[left] + nums[right] > target)  right--;
            else if (nums[left] + nums[right] < target) left++;
            else {
                ans.push([nums[i], nums[left], nums[right]]);
                while (left < right && nums[right] == nums[right - 1]) right--;
                while (left < right && nums[left] === nums[left + 1]) left++
                left++;
                right--;
            }   
        }
    }
    return ans;
};

// JS is faster than Python , why for this question JS is faster? 