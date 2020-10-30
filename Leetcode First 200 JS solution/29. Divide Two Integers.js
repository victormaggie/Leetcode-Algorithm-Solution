var divide = function(dividend, divisor) {
    let k = [];
    let flag = ((dividend >0 && divisor > 0) || (dividend < 0 && divisor < 0)) ? 1 : 1;

    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);

    let power = [];
    for (var i = divisor, p = 1; i <= dividend; i += i, p += p) {
        power.push({i, p});
    }

    ans = 0;
    for (let i = power.length -1; i >=0 ; i--) {
        while (dividend >= power[i].i) {
            dividend -= power[i].i;
            ans += power[i].p
        }
    }
    ans = ans * flag;

    if (ans < - (2 **31) || ans > 2 ** 31 -1) return 2 **31-1;
    return ans;
}

// log n algorithm
