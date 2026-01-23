#include <vector>
using namespace std;

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int n = nums.size();
        int curr_max_length = 1;
        int max_length = 1;
        for (int i = 0; i < n - 1; i++)
        {
            if (nums[i] < nums[i + 1])
            {
                curr_max_length++;
            }
            else
            {
                curr_max_length = 1;
            }
            max_length = std::max(max_length, curr_max_length);
        }
        return max_length;
    }
};