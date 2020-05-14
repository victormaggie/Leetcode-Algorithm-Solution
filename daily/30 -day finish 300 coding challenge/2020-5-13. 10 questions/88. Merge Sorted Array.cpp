#include<vector>
#include<iostream>
using namespace std;

class Solution{
public:
    void merge(vector<int> &nums1, int m, vector<int> & nums2, int n){
        int p1 = m - 1, p2 = n - 1, p = m + n -1;
        while (p1 >= 0 and p2 >= 0){
            if (nums1[p1] and nums2[p2]){
                nums1[p] = nums2[p2];
                p2 --;
            }
            else{
                nums1[p] = nums1[p1];
                p1 --;
            }
        p --;
        }
        for (int c = 0; c < p2 + 1; c++){
            nums1[c] = nums2[c];
        }
    }
};

// time complexity o(n)
// spacee complexity o(1)
