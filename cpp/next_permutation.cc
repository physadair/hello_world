#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using std::cout;
using std::endl;
using std::swap;
using std::reverse;
using std::vector;

class Solution {
public:
    void nextPermutation(vector<int>& nums) 
    {
        for (int i=nums.size()-2; i>=0; --i) {
            for (int j=nums.size()-1; j>i; --j) {
                if (nums[i]<nums[j]) {
                    swap(nums[i], nums[j]);
                    reverse(nums.begin()+i+1, nums.end());
                    return;
                }
            }
        }
        reverse(nums.begin(), nums.end());

    }
};

int main()
{
    //vector<int> nums {1, 2, 3, 4, 5, 6, 7, 8};
    vector<int> nums {1};
    for (int i=0; i<10; ++i) {
        Solution().nextPermutation(nums);
        for (auto n: nums)
            cout << n << " ";
        cout << endl;
    }

    return 0;
}
