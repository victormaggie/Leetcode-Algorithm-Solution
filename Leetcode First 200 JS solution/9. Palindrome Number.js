var isPalindrome = function(x) {
    if (x < 0) return false;
    let ans = 0;
    let value = x;

    while (x) {
        ans = ans * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    return ans === value;
};

// o(n)
//o(1)
