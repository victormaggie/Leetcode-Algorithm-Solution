/**
 * @param {number[]} w
 */
var Solution = function(w) {
    
    // binary search method here
    
    const sum = w.reduce((a,b) => a + b, 0);

    this.stack = [];
    let prefix = 0;
    for (let char of w){
        prefix += (char / sum);   
        this.stack.push(prefix);
    }
};

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function() {
    
    let left = 0, right = this.stack.length-1;
    let random = Math.random();
    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        if (this.stack[mid] <= random){
            left = mid + 1;
        } else {
            right = mid-1;
        }
    }
    
    return left;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
