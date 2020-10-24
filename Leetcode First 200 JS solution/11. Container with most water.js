var maxArea = function(height) {
    let ans = 0;
    let left = 0, right = height.length - 1;
    while (left < right){
        const distance = right - left;
        const volume = Math.min(height[left], height[right]) * distance;
        ans = Math.max(ans, volume);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return ans;
}

// o (n) solution 
