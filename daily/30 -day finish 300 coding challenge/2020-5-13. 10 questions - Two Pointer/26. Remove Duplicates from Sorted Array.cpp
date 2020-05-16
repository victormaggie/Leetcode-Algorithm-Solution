#include<vector>
using namespace std;
class Solution{
public:
    int removeDuplicates(vector<int>& nums){
        if (nums.size() == 0) return 0;
        int i = 0;
        for (int c = 1; c < nums.size(); c++){
            if (nums[i] != nums[c]){
                i ++;
                nums[i] = nums[c];
            }
        }
        return i + 1;
    }
};
