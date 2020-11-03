var twoSum = function(nums, target) {

    let hashmap = {};
    for (let i = 0; i < nums.length; i++) {
        if ((target - nums[i] in hashmap)) return [hashmap[target-nums[i]], i];
        hashmap[nums[i]] = i;
    }
}

// o(n) solution here
