/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    
    if (divisor == 0) return 2** 31 -1;
    
    let flag = ((dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0)) ? 1 : -1;
    
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    
    let stack = [];
    
    // divident = 2 ^ 0 * divisor + 2 ^ 1 * divisor + 2 ^ 2 * divisor .......
    
    for (let i = divisor, p = 1; i <= dividend; i += i, p += p) {
        stack.push({i, p});
    }
    
    ans = 0;
    for (let i = stack.length-1; i >= 0; i--) {
        if (dividend >= stack[i].i) {
            dividend -= stack[i].i;
            ans += stack[i].p
        }
    }
    
    ans = ans * flag;
    if (ans < -(2 **  31) || ans > (2 ** 31 -1)) return 2**31-1 ;
    return ans;
};


// log (K) solution.
