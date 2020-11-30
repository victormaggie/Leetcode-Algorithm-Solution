var trap = function(height) {
    let stack = [];
    let area = 0;

    // o(1) monotonic stack solution !
    // the code 

    for (let i = 0; i < height.length; i++) {
        while (stack.length && height[i] > height[stack.slice(-1)] ) {
            const top = stack.slice(-1);
            stack.pop();
            if (stack.length == 0) break;
            const h = Math.min(height[stack.slice(-1)], height[i]) - height[top];
            const d = i - stack.slice(-1) - 1;
            area += d * h;
        }
        stack.push(i);
    }
    return area;
}