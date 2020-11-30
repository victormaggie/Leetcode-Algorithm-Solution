using namespace std;

#include<iostream>
#include<vector>

class Knapsack{
public:
    int solveKnapsack(const vector<int> &profits, const vector<int> &weights, int capacity){
        return this->knapsackRecursive(profits, weights, capacity, 0);
    }

// Brute force solution
private:
    int knapsackRecursive(const vector<int> &profits, const vector<int> &weights, int capacity, int currentIndex){
        // base checks
        if (capacity <=0 || currentIndex >= profits.size()){
            return 0;
        }

        // recursive call after choosing the element at the currentIndex
        // If the weight of the element at CurrentIndex exceeds the capacity, we donot process it

        int profit1 = 0;
        if (weights[currentIndex] <= capacity){
            profit1 = 
                profits[currentIndex] + 
                knapsackRecursive(profits, weights, capacity - weights[currentIndex], currentIndex + 1);
        }

        // recursive call excluding the element at currentIndex
        int profit2 = knapsackRecursive(profits, weights, capacity, currentIndex+1);

        return max(profit1, profit2);
    }
};


class Knapsack_Top_Down{
public:
    int solveKnapsack(const vector<int> &profits, const vector<int> &weights, int capacity){
        vector<vector<int>> dp(profits.size(), vector<int>(capacity+1, -1));
        return this->knapsackRecursive(dp, profits, weights, capacity, 0);
    }

private:
    int knapsackRecursive(vector<vector<int>> &dp, const vector<int> &profits,
                            const vector<int> &weights, int capacity, int currentIndex){
        // base 
        if (capacity <= 0 || currentIndex >= profits.size()){
            return 0;
        }
        // if we have already Memoization for the recursion!
        if (dp[currentIndex][capacity] != -1){
            return dp[currentIndex][capacity];
        }
        // recursive call after choosing the element at the CurrentIndex
        // if we weight of the element at currentIndex exceeds the capacity, we should stops
        int profit1 = 0;
        if (weights[currentIndex] <= capacity){
            profit1 = profits[currentIndex] + knapsackRecursive(dp, profits, weights, 
                                                                capacity - weights[currentIndex],
                                                                currentIndex + 1);
        }
        int profit2 = knapsackRecursive(dp, profits, weights, capacity, currentIndex + 1);
        dp[currentIndex][capacity] = max(profit1, profit2);
        return dp[currentIndex][capacity];
        }
};

// time complexity o(N*C)
// space complexity o(N*C + n)
class Knapsack_Bottom_Up{
public:
    int solveKanpsack(const vector<int> &profits, const vector<int> &weights, int capacity){
        // basic checks
    if (capacity <= 0 || profits.empty() || weights.size() != profits.size()){
        return 0;
    }
    int n = profits.size();
    vector<vector<int>> dp(n, vector<int>(capacity + 1));

    // Initialization the dp array
    for (int i = 0; i < n; i++){
        dp[i][0] = 0;
    }
    // if we have only one weight, we will take it if it is not more than the capacity
    for (int c = 0; c <= capacity; c++){
        if (weights[0] <= c){
            dp[0][c] = profits[0];
        }
    }

    // process all sub-arrays for all the capacity
    for (int i = 1; i < n; i++){
        for (int c = 1; c <= capacity; c++){
            int profit1 = 0, profit2 = 0;
            if (weights[i] <= c){
                profit1 = profits[i] + dp[i - 1][c - weights[i]];
            }
            profit2 = dp[i - 1][c];
            // take maximum
            dp[i][c] = max(profit1, profit2);
        }
    }

    //return the bottom right corner
    return dp[n - 1][capacity];

    }

private:
    void printSelectedElements(vector<vector<int>> &dp, const vector<int> &weights,
                                const vector<int> &profits, int capacity){
    cout << "Selected weights:";
    int totalProfit = dp[weights.size()-1][capacity];
    for (int i = weights.size()-1; i > 0; i--){
        if (totalProfit != dp[i - 1][capacity]){
            cout << " " << weights[i];
            capacity -= weights[i];
            totalProfit -= profits[i];
        }
    }
    if (totalProfit != 0){
        cout << " " << weights[0];
    }
    cout << "" << endl;
    }
};

int main(int argc, char *argv[]){
    Knapsack ks;
    vector<int> profits = {1, 6, 10, 16};
    vector<int> weights = {1, 2, 3, 5};
    int maxProfit = ks.solveKnapsack(profits, weights, 7);
    cout << "Total knapsack profit ---> " << maxProfit << endl;
};

// space optimization
class Knapsack_space_optimization{
public:
    int solveKnapsack(const vector<int> &profits, const vector<int> &weights, int capacity){
        // basic checks
    if (capacity <= 0 || profits.empty() || weights.size() != profits.size()){
        return 0;
    }
    int n = profits.size();
    // we only need one previous row to find the optimal solution, overall we need '2', rows
    vector<vector<int>> dp(2, vector<int>(capacity+1));
    // if we have only one weight, we will take it if it is not more than the
    for (int c = 0; c <= capacity; c++){
        if (weights[0] <= 0){
            dp[0][c] = dp[1][c] = profits[0];
        }
    }
    // process all sub-array for all the capacities
    for (int i = 1; i < n; i++){
        for (int c = 0; c <= capacity; c++){
            int profit1 = 0, profit2 = 0;
            if (weights[i] <= c){
                profit1 = profits[i] + dp[(i-1)%2][c-weights[i]];
            }
            profit2 = dp[(i - 1)%2][c];
        }
    }
    return dp[(n - 1)%2][capacity];
    }
};

// the best optimal solution
class Knapsack_best{
public:
    int solveKnapsack(const vector<int> &profits, vector<int> &weights, int capacity){
        // basic checks
        if (capacity <= 0 || profits.empty() || weights.size() != profits.size()){
            return 0;
        }
    int n = profits.size();
    vector<int> dp(capacity + 1);
    // capacity
    for (int c = 0; c <= capacity; c++){
        if(weights[0] <= c){
            dp[c] = profits[0];
        }
    }
    //process all sub-arrays for all the capacities
    for (int i = 1; i < n; i++){
        for (int c = capacity; c >= 0; c--){
            int profit1 = 0, profit2 = 0;
            if (weights[i] <= c){
                profit1 = profits[i] + dp[c - weights[i]];
            }
            // exclude the item
            profit2 = dp[c];
            dp[c] = max(profit1, profit2);
        }
    }
    return dp[capacity];
    }
};
