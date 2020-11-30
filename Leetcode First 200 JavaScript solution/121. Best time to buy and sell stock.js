var maxProfit = function(prices) {

    if (prices.length === 0) return 0;
    let profit = 0, buy = prices[0];

    for (let price of prices) {
        const diff = price - buy;
        profit = Math.max(diff, profit);
        buy = Math.min(buy, price);
    }
    return profit;
}

// o(n) solution here!