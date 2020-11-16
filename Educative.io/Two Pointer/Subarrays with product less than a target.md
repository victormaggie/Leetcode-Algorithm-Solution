
- Given an array with positive numbers and a target number , find all of its contiguous subarray whose product is less than the target number


LC . 713 Subarray Product Less Than K

var numSubarrayProductLessThanK = function(nums, k) {
    let cnt = 0, product = 1;
    for (let i = 0, j = 0; i < nums.length; i++) {
        product *= nums[i];
        while (product >= k) product /= nums[j++];
        cnt += i - j + 1
    }
    return cnt > 0 ? cnt : 0;
}

`sliding window solution here!`


```
function find_subarrays(arr, target) {
  let result = [],
    product = 1,
    left = 0;
  for (right = 0; right < arr.length; right++) {
    product *= arr[right];
    while ((product >= target && left < arr.length)) {
      product /= arr[left];
      left += 1;
    }
    // since the product of all numbers from left to right is less than the target therefore,
    // all subarrays from left to right will have a product less than the target too; to avoid
    // duplicates, we will start with a subarray containing only arr[right] and then extend it
    const tempList = new Deque();
    for (let i = right; i > left - 1; i--) {
      tempList.unshift(arr[i]);
      result.push(tempList.toArray());
    }
  }
  return result;
}

```