
Given an array of unsorted numbers and a target sum, count all the triplet of which sum is less than target.

`Input: [-1, 0, 2, 3]`
`Target: 3`
`Output: 2`

LC 259.

```
var threeSumSmaller = function(nums, target) {
    
    // no need to consider duplicate, cuz we are only think about the index shit!
    let cnt = 0;
    nums.sort((a,b) => a-b);
    
    for (let i = 0; i < nums.length-2; i++) {

        let left = i + 1, right = nums.length-1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            
            if (sum < target) {
                cnt += right - left;
                left ++;
            } else right --;
        }
    }
    return cnt;
};

```