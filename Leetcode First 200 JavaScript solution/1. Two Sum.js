
var twoSum = function(nums, target){
    let hashmap = new Map();
    let ans = [];

    for (let i = 0; i < nums.length; i++) {
        if (hashmap.has(target - nums[i])) {
            // object property with a specific key is much faster than creating
            // a Map or using get
            ans.push(...[i, hashmap.get(target - nums[i])]);
            break;
        }
        hashmap.set(nums[i], i);
    }
    return ans;
}

// time complexity o(n)
// space complexity o(n)

// using object

var twoSum = function(nums, target) {
    let hashmap = {};
    for (let i = 0; i < nums.length; i++) {
        const key = target - nums[i];
        if (key in hashmap) {
            return [i, hashmap[key]];
        }
        hashmap[nums[i]] = i;
    }
}
