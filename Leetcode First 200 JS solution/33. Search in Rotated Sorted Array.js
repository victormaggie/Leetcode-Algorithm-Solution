var search = function(nums, target) {
    // binary search
    

    let left = 0, right = nums.length-1;
    const n = nums.length-1
    while (left <= right) {
        
        const mid = left + Math.floor((right - left) /2);
        
        if (nums[mid] === target) return mid;
        
        // left side
        else if (nums[mid] >= nums[0]) {
            if (nums[mid] > target && target >= nums[0]) right = mid - 1;
            else left = mid + 1;
        } 
        else {
            if (nums[mid] < target && target <= nums[n]) left = mid + 1;
            else right = mid - 1;
        }
    }
    return -1;
};

// divid into 3 parts ! here!!
