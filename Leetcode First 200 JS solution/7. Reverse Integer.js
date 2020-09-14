var reverse = function(x) {
    let ans = 0;

    while (x) {
        const digit = x % 10;
        ans = ans * 10 + digit;
        x = parseInt(x / 10);
    }
    if (ans >= 2 ** 31 -1 || ans <= -(2**31)) return 0;
    ans = x < 0 ? -ans : ans;
    return ans;
};

// o(n)

const reverse = x => {
    const limit = 21474883648;
    const k = x < 0 ? -1 : 1;
    const n = Number(String(Math.abs(x)).split('').reverse().join(''));
    return n > limit ? 0 : n * k;
};

// o(n)
