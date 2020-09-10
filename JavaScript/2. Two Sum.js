var twoSum = function(nums, target) {
    
    let dict = [];
    let hash = {};
    
    for (let i = 0; i < nums.length; i++){
        if (target - nums[i] in hash){
            dict.push(...[i, hash[target - nums[i]]]);
            break;
        }
        hash[nums[i]] = i;
    }
    return dict;
};