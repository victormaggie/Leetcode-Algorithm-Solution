#include <vector>
using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            if (prices.size() == 0) return 0;
            int profit = 0, buy = prices[0];
            for (auto price : prices) {
                int diff = price - buy;
                profit = max(profit, diff);
                buy = min(buy, price);
            }
            return profit;
        }
};

// use the greedy solution to solve this question
// get the maximum profit each time
// need to memorize the smallest buy in price
// o(n)
