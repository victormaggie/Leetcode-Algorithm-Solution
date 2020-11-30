using namespace std;
#include<iostream>
#include<vector>

class Fibonacci{
public:
    virtual int CalculateFibonacci(int n){
        if (n==0) return 0;
        // tabulation
        vector<int> dp(n+1);
        dp[0] = 0;
        dp[1] = 1;
        for(int i = 2; i <= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
};

int main(int argc, char *argv[]){
    Fibonacci *fib = new Fibonacci();
    cout << '5th Fibonacci is --->' << fib->CalculateFibonacci(5) << endl;
}