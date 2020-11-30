#include<stdlib.h>
#include<iostream>
#include<math.h>
#include<vector>
#include<numeric>

using namespace std;

class Solution{
    
public:

// 1 dimension solution
    bool canPartition(vector<int>&nums){
        int sum = accumulate(nums.begin(), nums.end(), 0);
        const int N = nums.size();
        if (sum % 2 != 0) return false;
        int target = sum >>1;
        
        vector<bool> dp(sum+1, false);
        dp[0] = true;
        for (int num: nums){
            for (int j = target; j >= num; --j){
                dp[j] = dp[j] || dp[j - num];
            }
        }            
        return dp[target];
    }
};

// change to 2 dimension

    bool canPartition(vector<int>&nums){
        int sum = accumulate(nums.begin(), nums.end(), 0);
        const int N = nums.size();
        int target = sum >> 1;
        if (sum % 2 != 0) return false;

        vector<vector<bool>> dp(N+1, vector<bool>(sum+1, false));

        for (int j = 0; j <= target; j++){
            dp[0][j] = false;
        }

        dp[0][0] = true;
        for (int i = 1; i <= N; i++){
            for (int j = 0; j <= target; j++){
                if (j >= nums[i-1])
                    dp[i][j] = dp[i-1][j] || dp[i-1][j - nums[i-1]];
                else
                {
                    dp[i][j] = dp[i-1][j];
                }            
            }
        }
    };