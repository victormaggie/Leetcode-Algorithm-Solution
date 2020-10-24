
var reverse = function(x) {
    if (x === 0) return 0;
    const sign = x < 0 ? -1 : 1;
    x = Math.abs(x);
    while ( x % 10 === 0) {
        x = Math.floor(x / 10);
    }
    ans = 0;
    while (x) {
        ans = ans * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    if (ans > 0x7FFFFFFF) return 0;
    return ans * sign;
}

// o(n) --> 
// o(1) --> 